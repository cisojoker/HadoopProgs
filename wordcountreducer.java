package wordcount;
import java.util.*;
import java.io.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
public class reducer extends MapReduceBase implements Reducer(Text,IntWritable,Text,IntWritable){
  public void reduce(Text Key,Iterator<IntWritable>value,outputCollector<Text,IntWritable>output,Reporter r){
    int count=0;
    while(value.hasNext()){
      count+=value.next().get();
    }
    ouput.collect(new Text(key),new IntWritable(count));
  }
}
