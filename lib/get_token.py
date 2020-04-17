import requests
import json


class Req():

    token = {}

    @staticmethod
    def update_token():
        ret = requests.get(
            "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx963cab3f76c2a895&secret=607dee317bb50fab9196bb9c06cc3c1a")
        if ret.status_code == 0:
            Req.token = json.loads(ret.text)
        return ret

    @classmethod
    def give_token(cls):
        return cls.token.get("access_token")


if __name__ == '__main__':
    print(Req.token)
    Req.update_token()
    print(Req.token)
