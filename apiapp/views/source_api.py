#!/usr/bin/python3
# coding: utf-8
import hashlib
import uuid
from datetime import datetime

from flask import Blueprint
from flask import request, jsonify
from sqlalchemy import or_, and_, not_

from db import session
from apiapp.models import *

from common import code_, cache_, token_
from db.raw_ import query
from . import validate_json, validate_params
from common.serializor import to_json

blue = Blueprint('file_api', __name__)


@blue.route('/source/', methods=['GET'])
def article_img():
    user_id = cache_.get_user_id(request.args.get('token'))
    if user_id:
        try:
            ret1 = session.query(CArticle).filter(CArticle.u_id == user_id).all()
            ret2 = session.query(CImage).filter(CImage.i_id == ret1.i_id).all()
            return jsonify({
                'state': 0,
                'data': to_json((ret1,ret2))
            })
        except:
            pass

    return jsonify({
        'state': 1,
        'msg': '没有数据'
    })


@blue.route('/images/', methods=['GET'])
def list_images():
    user_id = cache_.get_user_id(request.args.get('token'))
    sql = """
       SELECT f.*, u.phone
       FROM t_file f
       JOIN t_user u ON f.user_id = u.user_id
       WHERE f.file_type = %s
       and u.user_id = %s
       """

    return jsonify({
        'state': 0,
        'data': query(sql, 1, user_id)
    })


