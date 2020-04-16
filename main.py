from flask import Flask
from flask import request, jsonify
from configparser import ConfigParser
import logging
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


@app.route("/wx", methods=["GET", "POST"])
def wx():

    if request.method == "POST":
        print(request.data)
        data = request.get_json()
        print(data)
        print(request.form)
        print(request.form.get("ToUserName"))
        print(request.form.get("FromUserName"))
        print(request.form.get("CreateTime"))
        print(request.form.get("MsgType"))
        print(request.form.get("Content"))
        print(request.form.get("MsgId"))
        return ""

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