import requests

from unittest import TestCase

HOST = 'localhost'
PORT = 5000

base_url = f'http://{HOST}:{PORT}'
data = {
    #'name':'liyusheng',
    'phone': '15706001062',
    'token': "cf36519d72aa54d0778d8b196453bb86"
}

class TestUserApi(TestCase):
    #获取验证码
    def test_a_send_code(self):
        url = base_url + f'/api/code/?phone={data["phone"]}'
        resp = requests.get(url)
        print(resp.json())

    #用户注册
    def test_b_regist(self):
        url = base_url + '/api/regist/'
        resp = requests.post(url, json={
            'name': 'liyusheng',
            'phone': '15706001062',
            'code':  '9384',
            'pwd': '123456'  # 密文要求（前端）：需要使用hash算法
        })
        print(resp.json())

    #用户登录
    def test_c_login(self):
        url = base_url + '/api/login/'
        resp = requests.post(url, json={
            'phone': data['phone'],
            'pwd': '654321'
        })
        resp_data = resp.json()
        print(resp_data)
        if resp_data['state'] == 0:
            data['token'] = resp_data['token']


    #用户修改密码
    def test_d_login(self):
        url = base_url + '/api/modify_auth/'
        resp = requests.post(url, json={
            'token': data['token'],
            'pwd': '654321',
            'new_pwd': '123456',
        })
        resp_data = resp.json()
        print(resp_data)

    #用户发表文章
    def test_up_article(self):
        url = base_url + '/api/upload_article/'
        resp = requests.post(url, json={
            'token': data['token'],
            'name': '秋天',
            'details': '秋风用时光的旋律，用桂花的芬芳、苹果的馨香、菊花的灿烂、牵牛花的奔放、一串红的艳丽，'
                       '把一望无际的田野乡村，演绎得在自然中沉醉，渲染得天地间空旷而又阳刚。'
        })
        resp_data = resp.json()
        print(resp_data)

class TestSourceCase(TestCase):
    #首页资源展示
    def test_home_source(self):
        url = base_url + '/api/home_source/'
        resp = requests.get(url)
        print(resp.json())

    def test_user_article(self):
        url = base_url + '/api/userarticle/'
        resp = requests.get(url)
        print(resp.json())