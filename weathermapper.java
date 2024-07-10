package weather;
import java.io.*;
import java.util.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
public class mapper extends MapReduceBase implements Mapper(LongWritable,Text,Text,DoubleWritable){
  public void map(LongWritable key,Text value,OutputCollector<Text,DoubleWritable>output,Reporter r)throws IOException{
    String line=value.toString();
    String year=line.substring(15,19);
    Double temp=Double.parseDouble(line.substring(87,92));
    output.collect(new Text(year),new DoubleWritable(temp));
  }
}
