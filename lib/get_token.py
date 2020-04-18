import requests
import json
import datetime
from db.sql import Sql


class Req():
    table = "token"

    @classmethod
    def update_token(cls):
        ret = requests.get(
            "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx963cab3f76c2a895&secret=607dee317bb50fab9196bb9c06cc3c1a")
        if ret.status_code == 200:
            token = json.loads(ret.text)
            token["table"] = cls.table
            token["id"] = 1
            token["updatetime"] = datetime.datetime.now().strftime("%Y-%m-%d %X")
            sql = Sql()
            sql.insert_or_update(token)
            sql.close()
        return

    @classmethod
    def give_token(cls):
        sql = Sql()
        sql.cursor.execute("select * from token where id = 1")
        ret = sql.cursor.fetchone()
        sql.close()
        return ret


if __name__ == '__main__':
    pass
