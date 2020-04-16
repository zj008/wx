import time

class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TestMsg(object):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict["ToUserName"] = toUserName
        self.__dict["FromUserName"] = fromUserName
        self.__dict["Content"] = content
        self.__dict["CreateTime"] = int(time.time())

    def send(self):
        xmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
        """
        return xmlForm.format(**self.__dict)


class ImageMsg(object):
    def __init__(self, toUserName, fromUserName, MediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = MediaId

    def send(self):
        xmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
            </xml>
        """
        return xmlForm.format(**self.__dict)


if __name__ == '__main__':
    t = ImageMsg("a", "b", "c")
    print(t.send())