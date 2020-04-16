from flask import Flask
from flask import request, jsonify
from configparser import ConfigParser
import logging
from lib import hs
from lib import parse

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
        data = request.data
        data = parse.parse_xml(data.decode("utf8"))
        c = data.get("content")
        print(c)
        if "0" in c:
            return "毒鸡汤"
        if "1" in c:
            return "讲个段子"

        return "请输入h 获取帮助列表"
    else:
        return auth(request)


def auth(req):
    signature = req.args.get("signature")
    timestamp = req.args.get("timestamp")
    nonce = req.args.get("nonce")
    echostr = req.args.get("echostr")
    token = cf.get("args", "token")
    list = [token, timestamp, nonce]
    hashcode = hs.s1(list)
    if hashcode == signature:
        return echostr
    else:
        return ""


if __name__ == '__main__':
    app.run(host=host, port=port)