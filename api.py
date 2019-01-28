# encoding=utf-8
"""
使用Python Flask完成一些简单的请求
"""
from flask import Flask, jsonify
from flask_restful import reqparse, Api, Resource, request
import requests, pymongo
import mongo_op

app = Flask(__name__)


@app.route('/getOpenid', methods=['POST'])
def get_openid():
    """
    :return: 用户的openid
    """
    code = request.form['code']
    parmas = {
        'appid': '',     # 此处填写小程序的id
        'secret': '',   # 此处填写开发的小程序的对应的密钥
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    r = requests.get(url, params=parmas)
    openid = r.json().get('openid', '')

    return openid


@app.route('/uploadinfo', methods=['POST'])
def upload():
    """
    :return: 使用MongoDB保存用户的openId和头像
    """
    openId = request.form['openid']
    avatarUrl = request.form['avatarUrl']
    result = mongo_op.upload_user(openId, avatarUrl)
    return jsonify(result)


@app.route('/getinfo', methods=['GET'])
def getinfo():
    """
    :return: 获取用户的信息
    """
    data = mongo_op.getInfo()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
