"""CourseWork Part B
"""
from mrjob.job import MRJob

class CourseWorkPB(MRJob):

# this class will define two additional methods: the mapper method goes here
    def mapper(self, _, line):
        fields = line.split(",")
        #Fields contains line as follows.
        #  0   1     2        3
        #hash, value, n    ,publicKey
        wallet = '{1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v}'
        try:
            if (len(fields)==4):
                publickey = fields[3]
                if publickey == wallet:
                    yield(line,1)
        except:
            pass

    def combiner(self, key, values):
        yield(key,sum(values))

    def reducer(self, key, values):
        print(key)


#this part of the python script tells to actually run the defined MapReduce job.
if __name__ == "__main__":
    CourseWorkPB.JOBCONF= { 'mapreduce.job.reduces': '3' }
    CourseWorkPB.run()
