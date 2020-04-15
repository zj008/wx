from flask import Flask
from configparser import ConfigParser

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
    return "this is handle wx"


if __name__ == '__main__':
    app.run(host=host, port=port)