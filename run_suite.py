# 1 导包
import time
import unittest
import app
# from script.login_test import LoginTest
from script.login_test_parame import LoginTest
from tools.HTMLTestRunner import HTMLTestRunner

# 2 生成测试套件
suite = unittest.TestSuite()

# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(LoginTest))

# 4 指定测试报告的地址
# report_path = app.BASE_DIR + "/report/ihrm-{}.html".format(time.strftime('%Y%m%d %H%M%S'))
report_path = app.BASE_DIR + "/report/ihrm.html"
# 5 使用HTMLTestRunner运行测试套件
with open(report_path, 'wb') as f:
    # 定义HTMLTestRunner的实例
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理系统", description="V1.0")
    # 使用runner实例运行测试套件
    runner.run(suite)