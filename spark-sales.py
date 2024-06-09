import sys
from pyspark import SparkContext
if(len(sys.argv)!=3):
    print("provide the valid input and output")
    sys.exit(0)
sc=SparkContext()
file=sc.textFile(sys.argv[1])
data=file.map(lambda x:(x.split(',')[7],1))
dd=data.countByKey()
d=dd.parallelize(dd.items())
d.saveAsTextFile(argsv[3])
