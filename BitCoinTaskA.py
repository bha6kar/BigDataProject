"""COURSEwork Part A
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import time

#regular expression to split into words 
WORD_REGEX = re.compile(r"\b\w+\b")

class courseWork(MRJob):

    def mapper(self, _, line):
        try:
            transactions = line.split(",")
            if len(transactions) == 5:
                tx_time = int(transactions[2])
                year = time.strftime("%Y", time.gmtime(tx_time))        #returns year from time
                month = time.strftime("%m", time.gmtime(tx_time))       #returns month from time
                yearInt = int(year)

                if yearInt >= 2009 and yearInt <= 2014:
                    yield ((year, month), 1)

        except:
            pass

    def combiner(self, key, values):
        yield (key, sum(values))

    def reducer(self, key, values):
        yield (key, sum(values))

#this part of the python script tells to actually run the defined MapReduce job.
if __name__ == '__main__':
    courseWork.run()
