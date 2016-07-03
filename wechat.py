# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import time
import hashlib
from xml.etree.ElementTree import *
from get_movie import *
from serch_movie import *


error_msg = '没有结果，请稍后再试'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def wechat_check():
    # 如果是GET请求，则是验证token,返回echostr
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
    # 获取请求的内容
    recv_xml = fromstring(request.data)
    ToUserName = recv_xml.find("ToUserName").text
    FromUserName = recv_xml.find("FromUserName").text
    recv_Content = recv_xml.find("Content").text
    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</Crea" \
            "teTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
    # 如果请求的是'类型'，则返回类型内容（包括全部）
    if recv_Content == '类型':
        for movie_type in movie_types:
            reply_context = movie_type+' '
    elif recv_Content in movie_types:
        reply_context = get_movie_info(recv_Content)
    else:
        reply_context = serch_movie(recv_Content)

    if reply_context == None:
        reply_context = error_msg
    response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())), reply_context))
    response.content_type = 'application/xml'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
