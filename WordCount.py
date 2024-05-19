from mrjob.job import MRJob

class MRWordcount(MRJob):
    def mapper(self,_,line):
       row=line.split()
       for word in row:
           yield word,1
        
    def reducer(self,key,value):
        yield row,sum(value)

if __name__=='__main__':
    MRWordcount.run()
