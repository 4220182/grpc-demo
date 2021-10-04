from concurrent import futures

import grpc

import userinfo_pb2_grpc
from userinfo_pb2 import UserReply

#这里只是简单定义一个响应消息，你可以根据你的要求，或使用从数据库中查询的结果。
userReplyInfo = UserReply(userId=5, desc="6")

'''
UserInfoService实现所有的UserInfo服务方法。
我们在proto中只定义了一个方法：GetUserInfo，这里是实现这个方法。
'''
class UserInfoService (userinfo_pb2_grpc.UserInfoServicer):
    #request 客户端发送的消息，类型是：proto中定义的UserRequest
    def GetUserInfo(self, request, context):
        print(context)
        #返回消息，类型是proto定义的消息类型:UserReply
        return userReplyInfo

'''
启动 gRPC 服务器，以便客户端可以实际使用您的服务
服务器start()方法是非阻塞的。将实例化一个新线程来处理请求。server.start()在此期间，线程调用通常不会有任何其他工作要做。
在这种情况下，您可以调用 server.wait_for_termination()干净地阻塞调用线程，直到服务器终止。
'''
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    userinfo_pb2_grpc.add_UserInfoServicer_to_server(
        UserInfoService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()