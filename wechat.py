# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import time
import hashlib
from xml.etree.ElementTree import *
from get_movie import *


error_msg = '没有结果，请稍后再试'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def wechat_check():
    print(request)
    if request.method == 'GET':
        token = 'wan1987'
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s).hexdigest() == signature:
            return make_response(echostr)

    recv_xml = fromstring(request.data)
    ToUserName = recv_xml.find("ToUserName").text
    FromUserName = recv_xml.find("FromUserName").text
    recv_Content = recv_xml.find("Content").text
    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</Crea" \
            "teTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"


    if recv_Content == '类型':
        reply_context = '全部'
        for movie_type in movie_types:
            reply_context = reply_context+','+movie_type
    else:
        reply_context = query_mysql(recv_Content)
    if reply_context == None:
        reply_context = error_msg
    response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())), reply_context))
    response.content_type = 'application/xml'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
