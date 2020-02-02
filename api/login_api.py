import requests
import  app

class LoginApi:

    def __init__(self):
        # 定义登录的url
        self.login_url = app.host + "/api/sys/login"
        # 定义登录的请求头
        self.headers = app.header

    def login (self, mobile,password):
        data = {
            "mobile":mobile,
            "password":password
        }
        return requests.post(url=self.login_url, json=data, headers=self.headers)

    def login_empty(self):
        return requests.post(url=self.login_url)

    def login_null_params(self,mobile,password,*args, **kwargs):
        data = {
            "mobile": mobile,
            "password": password
        }

        if kwargs:
            for k,v in kwargs.items():
                data[k] = v
        return requests.post(self.login_url, json=data, headers=self.headers)
