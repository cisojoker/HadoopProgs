import sys
from pyspark import SparkContext
if(len(sys.argv)!=3):
    print("provide the valid input and output")
    sys.exit(0)
sc=SparkContext()
file=sc.textFile(sys.argv[1])
temp=f.map(lambda x:(x.split('\t')[3],float(x.split('\t')[8])))
data=temp.reduceByKey(lambda a,b:a+b)
data.saveAsTextFile(sys.argv[2])

