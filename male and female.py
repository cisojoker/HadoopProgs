from mrjob.job import MRJob

class MREmployee(MRJob):
    def mapper(self,_,line):
       row=line.split("\t")
       gender=row[3]
       salary=float(row[8])
       yield gender,salary
       
        
    def reducer(self,key,value):
       totalsal=0
       cnt=0
       for v in value:
           totalsal+=v
           cnt+=1
       avgsal=totalsal/cnt
       yield "Gender: "+key,"total employees: "+str(cnt)+"Average Salary: "+str(avgsal)
           
if __name__=='__main__':
    MREmployee.run()
