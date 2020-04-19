from flask import Flask
from flask import request, jsonify
from configparser import ConfigParser
import logging
from lib import hs
from lib import receive, reply, parse
import os
from lib.get_token import Req
import time
from db.sql import Sql


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
        data = data.decode()
        rec = receive.parse_xml(data)
        if isinstance(rec, receive.Msg):
            toUser = rec.FromUserName
            fromUser = rec.ToUserName
            if rec.MsgType == "text":
                sql = Sql()
                rep = parse.parse_sed_content(sql, reply, toUser, fromUser, rec.Content)
                # rep = reply.TestMsg(toUser, fromUser, content)
                return rep.send()
                pass
            elif rec.MsgType == "image":
                mediaId = rec.MediaId
                rep = reply.ImageMsg(toUser, fromUser, mediaId)
                return rep.send()
            else:
                reply.Msg().send()
        else:
            print("暂不处理")
            return reply.Msg().send()
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
    # sql = Sql()
    # ret = parse.parse_sed_content(sql, "3")
    # print(ret)
    # sql.close()