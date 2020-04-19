import xml.etree.cElementTree as ET
import random

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

c = """
请输入数字获取相应内容：
    1 ： 获取一条毒鸡汤
    2 ： 获取一条真情告白
    3 ： 获取一条李诞经典语录
    4 :  获取精美壁纸一张
或者发送一张图片来斗图。
ps : 壁纸为缩略图，想要获取高清原图请去4k高清网自行下载
斗图功能待完成！
"""

def parse_sed_content(sql, reply, toUser, fromUser, text):
    text = text.strip()
    texts = [(c,)]
    if text.startswith("4"):
        ids = sql.select("select media_id from media")
        media_id = random.choice(ids)[0]
        rep = reply.ImageMsg(toUser, fromUser, media_id)
        return rep

    if text.startswith("1"):
        texts = sql.select("select text from texts where type = 'soup'")
    elif text.startswith("2"):
        texts = sql.select("select text from texts where type = 'confession'")
    elif text.startswith("3"):
        texts = sql.select("select text from texts where type = 'lidan'")
    content = random.choice(texts)[0]
    rep = reply.TestMsg(toUser, fromUser, content)
    return rep


if __name__ == '__main__':
    pass
