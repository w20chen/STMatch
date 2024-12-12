import sys
import os
import glob
from subprocess import Popen, PIPE, TimeoutExpired
import time


def generate_args(binary, *params):
    arguments = [binary]
    arguments.extend(list(params))
    return arguments


def execute_binary(args, timeout=240):  # timeout 240 sec
    try:  
        process = Popen(args, stdout=PIPE, stderr=PIPE, text=True)
        (std_output, std_error) = process.communicate(timeout=timeout)  
        rc = process.returncode
        return rc, std_output, std_error  
    except TimeoutExpired:  
        process.kill()
        std_output, std_error = process.communicate()
        print("Process timed out")
        return -1, "Process timed out", std_error


def check(binary_path, data_graph_path, query_graph_path):
    execution_args = generate_args(binary_path, data_graph_path, query_graph_path)

    start_time = time.time()
    (rc, std_output, std_error) = execute_binary(execution_args)
    end_time = time.time()

    elapsed_time = end_time - start_time

    if rc == 0:
        embedding_num = 0
        std_output_list = std_output.split('\n')
        for line in std_output_list:
            if 'Matches:' in line:
                embedding_num = int(line.split(':')[1].strip())
                break
        print('{0},{1},{2:.3f}'.format(int(query_graph_path.split('_')[-1]), embedding_num, elapsed_time))
    else:
        print('Query {0} execution error.'.format(query_graph_path))


if __name__ == '__main__':
    binary_path = './bin/fig_local_global_unroll.exe'
    data_path = '../gpu_subgraph_matching/test_enron/data_graph/data.graph'
    query_path = '../gpu_subgraph_matching/test_enron/query_graph/Q_'

    for i in range(100):
        check(binary_path, data_path, query_path + str(i))
