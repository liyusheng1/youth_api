import requests

from unittest import TestCase

HOST = 'localhost'
PORT = 5000

base_url = f'http://{HOST}:{PORT}'
data = {
    #'name':'liyusheng',
    'phone': '15706001062',
    'token': "79fd44bf5da19b38682ce029031c7b28"
}

class TestUserApi(TestCase):
    def test_a_send_code(self):
        url = base_url + f'/api/code/?phone={data["phone"]}'
        resp = requests.get(url)
        print(resp.json())
    def test_b_regist(self):
        url = base_url + '/api/regist/'
        resp = requests.post(url, json={
            'name': 'liyusheng',
            'phone': '15706001062',
            'code':  '9384',
            'pwd': '123456'  # 密文要求（前端）：需要使用hash算法
        })
        print(resp.json())

    def test_c_login(self):
        url = base_url + '/api/login/'
        resp = requests.post(url, json={
            'phone': data['phone'],
            'pwd': '123456'
        })
        resp_data = resp.json()
        print(resp_data)
        if resp_data['state'] == 0:
            data['token'] = resp_data['token']

    def test_d_login(self):
        url = base_url + '/api/modify_auth/'
        resp = requests.post(url, json={
            'token': data['token'],
            'pwd': '123456',
            'new_pwd': '654321',
        })
        resp_data = resp.json()
        print(resp_data)

    def test_up_article(self):
        url = base_url + '/api/upload_article/'
        resp = requests.post(url, json={
            'token': data['token'],
            'name': '夏天',
            'details': '秋风用时光的旋律，用桂花的芬芳、苹果的馨香、菊花的灿烂、牵牛花的奔放、一串红的艳丽，'
                       '把一望无际的田野乡村，演绎得在自然中沉醉，渲染得天地间空旷而又阳刚。'
        })
        resp_data = resp.json()
        print(resp_data)