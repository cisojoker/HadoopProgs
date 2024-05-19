from mrjob.job import MRJob
import csv
class MRSales(MRJob):
    def mapper(self,_,line):
        row=next(csv.reader([line]))
        price = float(row[2])
        product = row[1]
        card_type = row[3]
        country = row[7]
   
        yield "Country"+coutry,price
        yield "Product"+product,1
        yield "Card"+card_type,1
        
    def reducer(self,key,value):
        total=0
        for value in values:
            if "Country" in key:
                total+=value
            elif "Product" in key:
                total+=1
            elif "Card" in key:
                total+=1
        
        yield key,total

if __name__=='__main__':
    MRSales.run()
