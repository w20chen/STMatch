import sys
import os
import glob
from subprocess import Popen, PIPE
import time


def generate_args(binary, *params):
    arguments = [binary]
    arguments.extend(list(params))
    return arguments


def execute_binary(args):
    process = Popen(' '.join(args), shell=True, stdout=PIPE, stderr=PIPE)
    (std_output, std_error) = process.communicate()
    process.wait()
    rc = process.returncode
    return rc, std_output, std_error


def check_correctness(binary_path, data_graph_path, query_graph_path, expected_embedding_num):
    execution_args = generate_args(binary_path, data_graph_path, query_graph_path)

    start_time = time.time()
    (rc, std_output, std_error) = execute_binary(execution_args)
    end_time = time.time()

    elapsed_time = end_time - start_time

    if rc == 0:
        embedding_num = 0
        std_output_list = std_output.decode().split('\n')
        for line in std_output_list:
            if 'Matches:' in line:
                embedding_num = int(line.split(':')[1].strip())
                break
        if embedding_num != expected_embedding_num:
            print('Query {0} is wrong. Expected {1}, Output {2}'.format(query_graph_path, expected_embedding_num,
                                                              embedding_num))
            return
        print('pass {0}:{1}'.format(query_graph_path, embedding_num))
        print('Time taken: {:.2f} seconds'.format(elapsed_time))
    else:
        print('Query {0} execution error.'.format(query_graph_path))
        return


if __name__ == '__main__':
    binary_path = './bin/fig_local_global_unroll.exe'

    input_expected_results = []
    input_expected_results_file = '../gpu_subgraph_matching/test_naive/expected_output.txt'
    with open(input_expected_results_file, 'r') as f:
        for line in f:
            if line:
                input_expected_results.append(int(line.strip()))

    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_0.graph', input_expected_results[0])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_1.graph', input_expected_results[1])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_2.graph', input_expected_results[2])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_3.graph', input_expected_results[3])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_4.graph', input_expected_results[4])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_5.graph', input_expected_results[5])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_6.graph', input_expected_results[6])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_7.graph', input_expected_results[7])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_8.graph', input_expected_results[8])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_9.graph', input_expected_results[9])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_10.graph', input_expected_results[10])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_11.graph', input_expected_results[11])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_12.graph', input_expected_results[12])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_13.graph', input_expected_results[13])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_14.graph', input_expected_results[14])
    check_correctness(binary_path, '../gpu_subgraph_matching/test_naive/data_graph/D_0.graph', 
        '../gpu_subgraph_matching/test_naive/query_graph/Q_15.graph', input_expected_results[15])
