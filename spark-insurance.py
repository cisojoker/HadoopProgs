import sys
from pyspark import SparkContext
if(len(sys.argv)!=3):
    print("provide the valid input and output")
    sys.exit(0)
sc=SparkContext()
file=sc.textFile(sys.argv[1])
temp=f.map(lambda x:(x.split(',')[16],1))
dd=temp.countByKey()
d=sc.parallelize(dd.items())
d.saveAsTextFile(sys.argv[2])
