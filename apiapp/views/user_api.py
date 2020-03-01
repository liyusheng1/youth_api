
from datetime import datetime

from flask import Blueprint, Response
from flask import request, jsonify
from sqlalchemy import or_, and_, not_

from db import session
from apiapp.models import *
from common import code_, cache_, token_
from . import validate_json, validate_params

blue = Blueprint('user_api', __name__)


@blue.route('/code/', methods=['GET'])
def get_code():
    phone = request.args.get('phone')
    if phone:
        code_.send_code(phone)
        return jsonify({
            'state': 0,
            'msg': '验证码已发送'
        })

    return jsonify({
        'state': 1,
        'msg': '手机号不能为空'
    })


@blue.route('/regist/', methods=['POST'])
def regist():
    # 要求JSON数据格式：
    valid_fields = {"name", "phone", "code", "pwd"}
    data = request.get_json()  # 获取上传的json数据
    if data is None:
        return jsonify({
            'state': 4,
            'msg': '必须提供json格式的参数'
        })


    # 验证参数的完整性
    if set(data.keys()) == valid_fields:
        # 验证输入的验证码是否正确
        if not code_.valid_code(data['phone'], data['code']):
            return jsonify({
                'state': 2,
                'msg': '验证码输入错误，请确认输入的验证码'
            })

        user = User()
        user.name = data.get('name')
        user.phone = data.get('phone')
        user.pwd = data.get('pwd')
        user.create_time = datetime.now()

        session.add(user)
        session.commit()

    else:
        return jsonify({
            'state': 1,
            'msg': '参数不完整，详情请查看接口文档'
        })

    return jsonify({
        'state': 0,
        'msg': '注册成功',
        'data': data
    })

@blue.route('/login/', methods=['POST'])
def login():
    resp = validate_json()
    if resp: return resp

    resp = validate_params('phone', 'pwd')
    if resp: return resp

    data = request.get_json()
    try:
        user = session.query(User).filter(User.phone == data['phone'],
                                           User.pwd == data['pwd']).one()

        token = token_.gen_token(user.u_id)
        cache_.add_token(token, user.u_id)

        resp: Response = jsonify({
            'state': 0,
            'msg': '登录成功',
            'token': token
        })

        # 设置响应对象的cookie，向客户端响应cookie
        resp.set_cookie('token', token)
        return resp
    except:
        pass

    return jsonify({
        'state': 4,
        'msg': '用户名或口令输入错误',
    })


@blue.route('/modify_auth/', methods=['POST'])
def modify_auth():
    resp = validate_json()
    if resp: return resp

    resp = validate_params('new_pwd', 'pwd', 'token')
    if resp: return resp

    data = request.get_json()

    try:
        u_id = cache_.get_user_id(data['token'])
        if not u_id:
            jsonify({
                'state': 3,
                'msg': '登录已期，需要重新登录并获取新的token',
            })

        user = session.query(User).get(int(u_id))
        if user.pwd == data['pwd']:
            user.pwd = data['new_pwd']
            session.add(user)
            session.commit()

            return jsonify({
                'state': 0,
                'msg': '修改成功'
            })
        return jsonify({
            'state': 4,
            'msg': '原口令不正确'
        })
    except:
        pass

    return jsonify({
        'state': 3,
        'msg': 'token已无效，尝试重新登录',
    })


#用户上传作品
@blue.route('/upload_article/', methods=['POST'])
def up_article():
    resp = validate_json()
    if resp: return resp

    resp = validate_params('name', 'details', 'token')
    if resp: return resp

    data = request.get_json()  # 获取上传的json数据
    if data is None:
        return jsonify({
            'state': 4,
            'msg': '请输入完整的JSON'
        })
    details = data.get('details')
    print(details)
    if details:
        print(data['name'],data['details'])
        user_id = cache_.get_user_id(data['token'])
        article = CArticle()
        article.name = data.get('name')
        article.details = data.get('details')
        article.u_id = user_id
        session.add(article)
        session.commit()

        return jsonify({
            'state': 0,
            'msg': '提交成功，待审核',
            'data': data
        })
    return jsonify({
        'state': 2,
        'msg': '内容不能为空'
    })