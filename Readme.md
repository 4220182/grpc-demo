python3.9 -m pip install -r ./requirements.txt

python3.9 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto

docker build . -f recommendations/Dockerfile -t koza/recommendations:0.0.1
docker build . -f marketplace/Dockerfile -t koza/marketplace:0.0.1

docker run --name recommendations -d -p 0.0.0.0:50051:50051/tcp koza/recommendations:0.0.1
docker run --name marketplace -d -p 0.0.0.0:8080:8080/tcp -e RECOMMENDATIONS_HOST=192.168.5.4 koza/marketplace:0.0.1
curl http://localhost:8080/ 