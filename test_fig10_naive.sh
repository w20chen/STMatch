#!/bin/bash
graph_path=./data/bin_graph/
pattern_path=./data/pattern/
patterns=(9.g  10.g  11.g  12.g  13.g  14.g  15.g  16.g)

echo "Naive"
for pattern in ${patterns[@]}
do
	./bin/fig_naive.exe ${1}/snap.txt ${pattern_path}/${pattern}
done
