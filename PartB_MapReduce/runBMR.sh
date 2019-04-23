#!/bin/bash
python PartB1.py -r hadoop --output-dir out --no-output hdfs://studoop.eecs.qmul.ac.uk/data/bitcoin/vout.csv
hadoop fs -getmerge out vout_filter.txt
hadoop fs -rm -r out
hadoop fs -mkdir input
hadoop fs -copyFromLocal vout_filter.txt input/vout_filter.txt

python PartB2.py -r hadoop --output-dir out --no-output hdfs://studoop.eecs.qmul.ac.uk/data/bitcoin/vin.csv --file hdfs://studoop.eecs.qmul.ac.uk/user/bjs30/input/vout_filter.txt
hadoop fs -getmerge out first_join.txt
hadoop fs -rm -r out
hadoop fs -copyFromLocal first_join.txt input/first_join.txt

python PartB3.py -r hadoop --output-dir out --no-output hdfs://studoop.eecs.qmul.ac.uk/data/bitcoin/vout.csv --file hdfs://studoop.eecs.qmul.ac.uk/user/bjs30/input/first_join.txt
hadoop fs -getmerge out result.txt
hadoop fs -rm -r out