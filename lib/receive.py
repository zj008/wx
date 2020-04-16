import xml.etree.cElementTree as ET


def parse_xml(data):
    if len(data) == 0:
        return None
    xml_data = ET.fromstring(data)
    msg_type = xml_data.find("MsgType").text
    if msg_type == "text":
        return TestMsg(xml_data)
    elif msg_type == "image":
        return ImageMsg(xml_data)


class Msg(object):
    def __init__(self, xml_data):
        self.ToUserName = xml_data.find("ToUserName").text
        self.FromUserName = xml_data.find("FromUserName").text
        self.CreateTime = xml_data.find("CreateTime").text
        self.MsgId = xml_data.find("MsgId").text
        self.MsgType = xml_data.find("MsgType").text


class TestMsg(Msg):
    def __init__(self, xml_date):
        Msg.__init__(self, xml_date)
        self.Content = xml_date.find("Content").text


class ImageMsg(Msg):
    def __init__(self, xml_date):
        Msg.__init__(self, xml_date)
        self.PicUrl = xml_date.find("PicUrl").text
        self.MediaId = xml_date.find("MediaId").text
