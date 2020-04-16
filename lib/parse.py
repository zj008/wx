import xml.etree.cElementTree as ET


def parse_xml(s):
    if len(s) == 0:
        return None
    data = dict()
    xml_data = ET.fromstring(s)
    data["msg_type"] = xml_data.find("MsgType").text
    data["content"] = xml_data.find("Content").text
    data["msg_id"] = xml_data.find("MsgId").text
    data["create_time"] = xml_data.find("CreateTime").text
    data["from_user_name"] = xml_data.find("FromUserName").text
    data["to_user_name"] = xml_data.find("ToUserName").text
    return data


if __name__ == '__main__':
    pass
