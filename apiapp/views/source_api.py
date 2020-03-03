#!/usr/bin/python3
# coding: utf-8

from flask import Blueprint
from flask import request, jsonify

from db import session
from apiapp.models import *

from common.serializor import to_json

blue = Blueprint('file_api', __name__)


@blue.route('/home_source/', methods=['GET'])
def article_img():

    ret1 = session.query(FirstSentence).all()  #从数据库获取
    if ret1:
        return jsonify({
            'state': 0,
            'data': to_json(ret1)
        })

    return jsonify({
        'state': 1,
        'msg': '没有数据'
    })

@blue.route('/userarticle/', methods=['GET'])
def user_article():
    ret1 = session.query(CArticle).all() #从数据库获取所有用户发表过的文章
    for ret in ret1:
        user = session.query(User).filter(User.u_id == ret.u_id).all()
        for u in user:
            ret.username = u.name
    if ret1:
        return jsonify({
            'state':0,
            'data': to_json(ret1)
        })

    return jsonify({
        'state': 1,
        'msg': '没有数据'
    })



