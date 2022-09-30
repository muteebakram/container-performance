# Message Broker Performance

## Redis

### Install Redis Container

```sh
docker pull redis
docker run -it --name redis-server -d redis
docker logs redis-container
docker exec -it redis-container bash
docker stop redis-server
```

### Build Docker Application

```sh
cd redis
docker build . -t redis-app:latest
```

### Create Docker network

1. Create new docker network

```sh
docker network create redis-net
docker network inspect redis-net
```

2. Get the docker Ipv4 address

```
docker network inspect redis-net | grep -i ipv4
```

3. Use that ipv4 address in code redis host.

### Run the containers

```sh
# Make sure redis server is running
docker run --name redis-server -p 6379:6379 --net=host redis
# Start the producer container
docker run -it --name "redis-app-producer" redis-app sh -c  "python3 main.py producer"
# Start the consumer container
docker run -it --name "redis-app-consumer" redis-app sh -c  "python3 main.py consumer"
```
