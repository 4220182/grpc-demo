```shell
cd marketplace 
python3.9 -m pip install -r ./requirements.txt

cd recommendations
python3.9 -m pip install -r ./requirements.txt
```

```shell
python3.9 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
```

```shell
docker build . -f recommendations/Dockerfile -t koza/recommendations:0.0.1
```

```shell
docker build . -f marketplace/Dockerfile -t koza/marketplace:0.0.1
```

```shell
docker run --name recommendations -d -p 0.0.0.0:50051:50051/tcp koza/recommendations:0.0.1
```

```shell
docker run --name marketplace -d -p 0.0.0.0:8080:8080/tcp -e RECOMMENDATIONS_HOST=192.168.5.4 koza/marketplace:0.0.1

```
```shell
curl http://localhost:8080/ 
```

```shell
https://towardsdatascience.com/local-development-set-up-of-postgresql-with-docker-c022632f13ea

docker run -d \
	--name dev-postgres \
	-e POSTGRES_PASSWORD=123456 \
	-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
        -p 5432:5432 \
        postgres:latest
                
```
