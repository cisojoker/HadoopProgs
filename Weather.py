from mrjob.job import MRJob
class MRWeather(MRJob):
    def mapper(self,_,line):
        row=str(line)
        year=int(row[15:19])
        temp=float(row[87:92])
        yield year,temp
        
    def reducer(self,key,value):
        maxtemp=-99999
        mintemp=99999
        
        for v in value:
            if v>maxtemp:
                maxtemp=v
            if v<mintemp:
                mintemp=v
                
        yield "year:"+str(key),("max temp:"+str(maxtemp)+"min temp: "+str(mintemp))
        
if __name__=='__main__':
    MRWeather.run()
