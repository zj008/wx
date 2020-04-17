import requests
import json


class Req():
    token = {}

    @classmethod
    def update_token(cls):
        ret = requests.get(
            "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx963cab3f76c2a895&secret=607dee317bb50fab9196bb9c06cc3c1a")
        if ret.status_code == 200:
            cls.token = json.loads(ret.text)
        return

    @classmethod
    def give_token(cls):
        return cls.token.get("access_token")


if __name__ == '__main__':
    print(Req.token)
    Req.update_token()
    print(Req.token)
