"""CourseWork Part B
"""
from mrjob.job import MRJob

class CourseWorkPB(MRJob):

    vin_table = {}

    def mapper_init(self):

        with open("first_join.txt") as firstJoin:
            for line in firstJoin:
                fields = line.split(",")
                #Fields contains line as follows.
                #  0   1         2     3
                #txid, tx_hash, vout, wallet
                if len(fields) == 4:
                    key = (fields[1],int(fields[2]))
                    self.vin_table[key] = fields[3]


    def mapper(self, _, line):
        fields = line.split(",")
        #Fields contains line as follows.
        #  0   1     2        3
        #hash, value, n    ,publicKey
        try:
            if (len(fields)==4):
                hash = fields[0]
                match_vout = int(fields[2])
                key = (hash,match_vout)
                value = float(fields[1])
                wallet = fields[3]
                #yield(self.vout_table[txid],1)
                if key in self.vin_table.keys():
                    yield('topten',(wallet,value))
        except:
            pass

    def combiner(self, key, values):
        slist = sorted(values,key=lambda x:x[1],reverse=True)
        if len(slist) > 10:
            slist = slist[0:10]

        for item in slist:
           yield('',item)

    def reducer(self, key, values):
        slist = sorted(values,key=lambda x:x[1],reverse=True)
        if len(slist) > 10:
            slist = slist[0:10]

        for item in slist:
           yield('',item)


#this part of the python script tells to actually run the defined MapReduce job.
if __name__ == "__main__":
    CourseWorkPB.JOBCONF= { 'mapreduce.job.reduces': '3' }
    CourseWorkPB.run()
