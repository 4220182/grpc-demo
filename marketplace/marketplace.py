# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

from account_pb2 import AccountRequest, AccountReply
from account_pb2_grpc import AccountInfoStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)

account_host = os.getenv("ACCOUNT_HOST", "localhost")
account_channel = grpc.insecure_channel(
    f"{account_host}:50050"
)
account_client = AccountInfoStub(account_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )

@app.route("/account")
def render_account():
    account_request = AccountRequest(username="test1")
    account_response = account_client.GetAccountInfo(account_request)
    print("response:", account_response.username)
    return render_template(
        "account.html",
        account=account_response,
    )

if __name__ == '__main__':
    print("started. url: 0.0.0.0:8080/")
    app.run(host="::", port=8080)
