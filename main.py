from flask import Flask
from flask import request
from configparser import ConfigParser
from lib import hs

import os
print(os.getcwd())
cf = ConfigParser()
cf.read("conf/conf")
host = cf.get("host", "host")
port = cf.get("host", "port")

app = Flask(__name__)


@app.route("/")
def hello_word():
    return "hello word"


@app.route("/wx")
def wx():
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    token = cf.get("args", "token")

    list = [token, timestamp, nonce]
    print(list)
    hashcode = hs.s1(list)

    if hashcode == signature:
        return echostr
    else:
        return ""


if __name__ == '__main__':
    app.run(host=host, port=port)
