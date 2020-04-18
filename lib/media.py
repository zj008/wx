# -*- coding: utf-8 -*-
# filename: media.py
# from basic import Basic
import urllib2
import poster.encode
from poster.streaminghttp import register_openers
import json


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


if __name__ == '__main__':
    myMedia = Media()
    accessToken = "32_4xm9tDoFt-U7v8gCuhil9145YrIpAhvFFU5HxxTCMk3V22vcFpv3ZZOQ4xV43N16xBg8_cOFXna3b9JD1Ccpi2w8aCGvIl4x26hd1gTAU19iKLe7zgw8OjxzV0RaNT23icEJvS7rcwWLu10tFEYeADAVUO"
    filePath = "/Users/aibyte/Documents/code/python/wx/images/1.jpg"  # 请安实际填写
    mediaType = "image"
    data = myMedia.upload(accessToken, filePath, mediaType)
    f = open("/Users/aibyte/Documents/code/python/wx/info/media.txt", "a")
    f.write(json.dumps(data))
    f.write("\n")
    f.close()