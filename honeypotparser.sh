#!/bin/bash

input=honeypot/final.csv
output=output

hadoop fs -rmr $output

echo "=====Hadoop Time======"
time hadoop jar /local/Hadoop/hadoop-1.1.2/contrib/streaming/hadoop-streaming-1.1.2.jar -file "/home/rialto1/venkatsrir/projects/nwen406/mapper.py" -mapper "/home/rialto1/venkatsrir/projects/nwen406/mapper.py" -file "/home/rialto1/venkatsrir/projects/nwen406/reducer.py" -reducer "/home/rialto1/venkatsrir/projects/nwen406/reducer.py" -input $input -output $output
if [ $? -ne 0 ]; then
    exit 1
fi
if [ -d $output ]; then
    rm -r $output
fi

echo "=====Moving Output======"
hadoop fs -get $output $output

echo "=====Creating Graph======"
cat $output/part-00000 | python dataToJson.py > data.json
mv data.json "/u/students/venkatsrir/public_html" && chmod 777 "/u/students/venkatsrir/public_html/data.json"
firefox "http://homepages.ecs.vuw.ac.nz/~venkatsrir"

