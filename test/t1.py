from flask import Flask
from flask import request
from configparser import ConfigParser
import hashlib

cf = ConfigParser()
cf.read("conf")
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
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print(hashcode, signature)
    if hashcode == signature:
        return echostr
    else:
        return "xxx"


if __name__ == '__main__':
    app.run(host=host, port=port)