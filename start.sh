docker-compose build 
docker-compose ps 
docker-compose up -d 

docker exec hadoop hdfs dfs -rm -r -f /input
docker exec hadoop hdfs dfs -rm -r -f /output
docker exec hadoop hdfs dfs -mkdir /input 
docker exec hadoop hdfs dfs -put /data/movies.csv /input 
docker exec hadoop ./data/namenode_entrypoint.sh
./visualise/extract.c

docker-compose down 
