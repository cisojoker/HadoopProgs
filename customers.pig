customers=LOAD 'customers.txt' USING PigStorage(',') as (id:int,name:chararray,age:int,city:chararray,salary:int);
orders=LOAD 'order.txt' USING PigStroage(',') as (oid:int,date:chararray,cid:int,amount:int);
joinresult=JOIN customers BY id, orders BY cid;
STORE joinresult INTO 'joinresutlt';
sort=ORDER joinresult BY age ASC;
STORE sort INTO 'sortoutput';
