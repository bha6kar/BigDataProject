#!/bin/bash
python BitCoinTaskA.py -r hadoop --output-dir out --no-output hdfs://studoop.eecs.qmul.ac.uk/data/bitcoin/transactions.csv
hadoop fs -getmerge out outputA/resultA.txt
hadoop fs -rm -r out
