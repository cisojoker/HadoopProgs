sdetail=LOAD 'student.txt' USING PigStorage(',') as (id:int,firstname:chararray,lastnane:chararray,age:int,phone:chararray,city:chararray);
filterdata=FILTER sdetail BY city=='Chennai';
groupdata=GROUP sdetail BY age;
STORE filterdata INTO 'output1';
STORE groupdata INTO 'output2';
