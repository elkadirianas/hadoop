#!/bin/bash

# Step 2: Remove old local file inside container if exists
docker exec hadoop rm -f /tmp/genre_count.txt

# Step 3: Get result from HDFS to inside the container
docker exec hadoop hdfs dfs -get /output/genre_count/part-00000 /tmp/genre_count.txt

# Step 4: Copy it from container to host
docker cp hadoop:/tmp/genre_count.txt ./genre_count.txt



python3 -m venv venv
source venv/bin/activate

python visualise/py_scripts/to_csv.py
echo "✅ Result saved to: genre_count.csv"

pip install matplotlib

python visualise/py_scripts/visualise.py

deactivate

rm -rf venv 
rm genre_count.txt

