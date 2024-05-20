from mrjob.job import MRJob
import csv
class MRInsurance(MRJob):
    def mapper(self,_,line):
        row=next(csv.reader([line]))
        name=row[2]
        yield name,1
        
    def reducer(self,key,values):
        yield "Building name"+key,"frequency:"+str(sum(values))
        
if __name__=='__main__':
    MRInsurance.run()
