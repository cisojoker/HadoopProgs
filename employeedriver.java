package employee;
import java.io.*;
import java.util.*;
import org.apache.hadoop.io*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.fs.Path;
public class driver{
  JobConf conf=new JobConf(driver.class);
  conf.setMapperClass(mapper.class);
  conf.setReducerClass(reducer.class);
  conf.setOutputKeyClass(Text.class);
  conf.setOutputValueClass(DoubleWritable.class);
  FileInputFormat.addInputPath(conf, new Path(args[0]));
  FileOutputFormat.setOutputPath(conf,new Path(args[1]));
jobClient.runJob(conf);
}
}
