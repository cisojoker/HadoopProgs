import sys
from pyspark import SparkContext
if(len(sys.argv)!=3):
    print("provid input and output path")
    sys.exit(0)
sc=SparkContext()
f=sc.textFile(sys.argv[1])
temp=f.map(lambda x:(int (x[15:19]),int(x[87:92])))
maxi=temp.reduceByKey(lambda a,b:a if a>b else b)
maxi.saveAsTextFile(sys.argv[2])
