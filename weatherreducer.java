package weather;
import java.io.*;
import java.util.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.io.*;
class reducer extends MapReduceBase implements Reducer<Text,DoubleWritable,Text,DoubleWritable>{
  public void reduce(Text key,Iterator<DoubleWritable> value,OutputCollector<Text,DoubleWritable>output,Reporter r)throws IOException{
    Double mi=99999.0;
    Double ma=-99999.0;
    while(value.hasNext()){
      Double temp=value.next().get();
      mi=Math.min(mi,temp);
      ma=Math.max(ma,temp);
    }
    output.collect(new Text("min temp at"+key),new DoubleWritable(mi));
    output.collect(new Text("max temp at"+key),new DoubleWritable(ma));
  }
}
      
