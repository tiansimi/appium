__author__ = 'HLTQ'
from appium import webdriver
import unittest
import HTMLTestRunner
class apptest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': "android",
            'deviceName': "3a26189 device",
            'platformVersion': "4.4",
            'appPackage': "healthcare.amp.equipmentmanagement",
            'appActivity': ".ui.activity.WelcomeActivity",
            'noReset': "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        '''测试登录界面'''
        self.driver.find_element_by_id("setting_button").click()
        self.driver.find_element_by_id("login_button").click()
if __name__ == "__main__":
    testsuit = unittest.TestSuite()
    testsuit.addTest(apptest("test_login"))
    fp = open("./result.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试结果",
                                           description="detail")
    runner.run(testsuit)
    fp.close()