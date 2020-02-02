import logging
import unittest
from api.login_api import LoginApi
from utils import assert_utils, read_login_data
from parameterized.parameterized import parameterized


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_login_data)
    def test01_login(self,mobile,password,status_code,success,code,message):
        # 发送登录请求
        response = self.login_api.login(mobile, password)
        logging.info("登录成功的数据: {}".format(response.json()))

        assert_utils(self, response, status_code, success, code, message)

    # 无请求参数
    def test04_no_parmas(self):
        response = self.login_api.login_empty()
        logging.info("请求参数为空: {}".format(response.json()))
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 多参
    def test07_more_parmas(self):
        response = self.login_api.login_null_params("13800000002", "123456", {"numoal": "heiheihei"})
        logging.info("无意义参数: {}".format(response.json()))
        assert_utils(self, response, 200, True, 10000, "操作成功！")
