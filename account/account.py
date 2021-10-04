import psycopg2
import os
from concurrent import futures
import grpc
import account_pb2_grpc
from account_pb2 import AccountReply

# 连接数据库
psql_host = os.getenv("POSTGRESQL_HOST", "localhost")
conn = psycopg2.connect(dbname="demo", user="postgres",
                        password="123456", host=f"{psql_host}", port="5432")

def getAccountFromDb() :
    # 创建cursor以访问数据库
    cur = conn.cursor()
    # 查询数据
    cur.execute("SELECT * FROM accounts where username='test1'")
    row = cur.fetchone()
    return AccountReply(userId=row[0], username=row[1], info=row[2])

class AccountServicer (account_pb2_grpc.AccountInfoServicer):
    def GetAccountInfo(self, request, context):
        print(request.username)
        return getAccountFromDb()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_pb2_grpc.add_AccountInfoServicer_to_server(
        AccountServicer(), server
    )
    server.add_insecure_port("[::]:50050")
    print("listen: 0.0.0.0:50050")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()