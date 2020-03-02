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

    ret1 = session.query(FirstSentence).all()
    if ret1:

        return jsonify({
            'state': 0,
            'data': to_json(ret1)
        })

    return jsonify({
        'state': 1,
        'msg': '没有数据'
    })





