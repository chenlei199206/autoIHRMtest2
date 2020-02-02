import json
from unittest import TestCase
from requests import Response

import app


def assert_utils(self, response, status_code, success, code, message):
    # self response返回值,status_code,success,code,message预期值
    '''
    @type self:TestCase
    @type  response:Response
    '''
    jsonData = response.json()
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertIn(message, jsonData.get("message"))

# 读取登录数据
def read_login_data():
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, encoding="utf-8") as f:
        #加载为json格式
        jsonData = json.load(f)
        login_data_list = []
        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            status_code = login_data.get("status_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            login_data_list.append(( mobile, password, status_code, success, code, message))

        return login_data_list

