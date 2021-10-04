import os
import grpc
from userinfo_pb2 import UserRequest
from userinfo_pb2_grpc import UserInfoStub

#定义gRPC服务器地址
host = os.getenv("USERINFO_HOST", "localhost")
channel = grpc.insecure_channel(
    f"{host}:50051"
)
#要调用服务方法，我们首先需要创建一个stub
client = UserInfoStub(channel)

def getuserinfo(username):
    #poto中，GetUserInfo方法要求的请求消息体：UserRequest
    request = UserRequest(username=username)
    #使用同步，调用gRPC服务的方法，RPC 调用等待服务器响应，并将返回响应或引发异常;你也可以使用异步方法调用。
    reply = client.GetUserInfo(request)
    return reply

if __name__ == '__main__':
    reply = getuserinfo("test")
    print(reply.userId, reply.desc)