#!/bin/bash
set -e

# Start HDFS services (if required in this container)
# /entrypoint.sh /run.sh &  # Optional if base image already handles startup

# Wait for HDFS to become available
echo "⏳ Waiting for HDFS to be ready..."
until hdfs dfs -ls / >/dev/null 2>&1; do
    sleep 2
done

# Create input directory if it doesn't exist
hdfs dfs -mkdir -p /input

# Move the CSV file to HDFS input directory
echo "📂 Uploading movies.csv to HDFS /input..."
hdfs dfs -put -f /data/movies.csv /input/

# Run the MapReduce job
echo "🚀 Starting MapReduce job..."
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
  -input /input/movies.csv \
  -output /output/genre_count \
  -mapper /jobs/mapper.py \
  -reducer /jobs/reducer.py

# Show the result
echo "📊 Genre count results:"
hdfs dfs -cat /output/genre_count/part-*
