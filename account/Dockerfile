#FROM python
FROM python:3.9-slim-buster

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY account/ /service/account/
WORKDIR /service/account
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/account.proto

EXPOSE 50050
ENTRYPOINT [ "python", "account.py" ]