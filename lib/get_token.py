import requests


class Req():
    @staticmethod
    def get_token():
        ret = requests.get(
            "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx963cab3f76c2a895&secret=607dee317bb50fab9196bb9c06cc3c1a")
        print(ret.text)
        return ret


if __name__ == '__main__':
    Req.get_token()
