# -*- coding: utf-8 -*-
# filename: media.py
# from basic import Basic
import urllib2
import poster.encode
from poster.streaminghttp import register_openers
import json
import os


class Media(object):
    def __init__(self):
        register_openers()

    # 上传图片
    def upload(self, accessToken, filePath, mediaType):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (
            accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        data = urlResp.read()
        print data
        return data


def run(filePath):
    myMedia = Media()
    accessToken = "32_U53IjKxTtnZUhixO0SlwFSatJQDHGZoXRIsypDPvvTbOEfjGR4dWlEsDW2g8ljvztQuVvk4R7TLkrHukPs18C0UcEdPQNU1evOklhY1EWkD2wMGD48ixqPjboROzjcuQQAVB_Q_DFevFDRDkRVAiAEANRW"
    # filePath = "/Users/aibyte/Documents/code/python/wx/images/1.jpg"  # 请安实际填写
    mediaType = "image"
    data = myMedia.upload(accessToken, filePath, mediaType)
    f = open("/Users/aibyte/Documents/code/python/wx/info/media.txt", "a")
    f.write(json.dumps(data))
    f.write("\n")
    f.close()

if __name__ == '__main__':
    base = "/Users/aibyte/Documents/code/python/wx/images"
    dirs = os.listdir(base)
    for f in dirs:
        file = os.path.join(base, f)
        run(file)