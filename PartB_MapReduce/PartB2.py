"""CourseWork Part B
"""
from mrjob.job import MRJob

class CourseWorkPB(MRJob):

    vout_table = {}

    def mapper_init(self):
        # run the job with --file input/vout_filter.txt as obtained from the part1 and copied into the input folder
        with open("vout_filter.txt") as voutFilter:
            for line in voutFilter:
                fields = line.split(",")
                #Fields contains line as follows.
                #  0   1     2        3
                #hash, value, n    ,publicKey
                key = fields[0]
                self.vout_table[key] = fields[3]


    def mapper(self, _, line):
        fields = line.split(",")
        #Fields contains line as follows.
        #  0   1         2
        #txid, tx_hash, vout
        try:
            if (len(fields)==3):
                txid = fields[0]
                #yield(self.vout_table[txid],1)
                if txid in self.vout_table.keys():
                    yield(line,self.vout_table[txid])
        except:
            pass

    def reducer(self, key, values):
        for value in values:
            print("{0},{1}".format(key,value))


#this part of the python script tells to actually run the defined MapReduce job.
if __name__ == "__main__":
    CourseWorkPB.JOBCONF= { 'mapreduce.job.reduces': '3' }
    CourseWorkPB.run()
