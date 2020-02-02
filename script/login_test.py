import logging
import  unittest
from api.login_api import LoginApi
from utils import  assert_utils


class  LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_login_success(self):
        # 发送登录请求
        response = self.login_api.login("13800000002","123456")
        logging.info("登录成功的数据: {}".format(response.json()))

        # jsondata = response.json()
        # self.assertEqual(200,  response.status_code)
        # self.assertEqual(True, jsondata.get("success"))
        # self.assertEqual(10000, jsondata.get("code"))
        # self.assertEqual("操作成功！", jsondata.get("message"))

        assert_utils(self, response, 200, True, 10000,"操作成功！")

    #用户名不存在
    def test02_user_no(self):
        response = self.login_api.login("13900000002","123456")
        logging.info("用户不存在: {}".format(response.json()))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    #密码错误
    def test03_password_error(self):
        response = self.login_api.login("13800000002","error")
        logging.info("密码错误: {}".format(response.json()))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    #无请求参数
    def test04_no_parmas(self):
        response = self.login_api.login_empty()
        logging.info("请求参数为空: {}".format(response.json()))
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    #用户名为空
    def test05_user_isnull(self):
        response = self.login_api.login("","error")
        logging.info("用户名为空: {}".format(response.json()))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    #密码为空
    def test06_password_isnull(self):
        response = self.login_api.login("13800000002","")
        logging.info("密码为空: {}".format(response.json()))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参
    def test07_more_parmas(self):
        response = self.login_api.login_null_params("13800000002", "123456", {"numoal":"heiheihei"})
        logging.info("无意义参数: {}".format(response.json()))
        assert_utils(self, response, 200, True, 10000,"操作成功！")

