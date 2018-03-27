__author__ = 'HLTQ'
from test_program.pages.basePages import Basepage
from selenium.webdriver.common.by import By
from test_program.common.em_Login import Login
import time
from selenium.webdriver.common.keys import Keys


class PlanGuanli(Basepage):
    url = "http://192.168.10.131:8000/EM/DevicePlan/List"
    username_Id = Login.username_Id
    psw_Id = Login.psw_Id
    login_button = Login.login_button

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    '''计划信息查询'''
    year_id = (By.ID, "Year")  # 年度筛选框
    bizeType_Xpath = (By.XPATH, ".//*[@id='BizType']/option[@value = '1']")  # 筛选框-业务类型筛选框养护
    biziTpe_kuang = (By.ID, 'BizType')
    planType_Xpath = (By.XPATH, ".//*[@id='PlanType']/option[@value = '1']")  # 筛选框-计划类型 年度计划

    def shaiXuan(self, username, psw):
        self.driver.get(self.url)
        self.clear_input(self.username_Id)
        self.send_keys(self.username_Id, username)
        self.clear_input(self.psw_Id)
        self.send_keys(self.psw_Id, psw)
        self.click(self.login_button)
        time.sleep(2)
        self.click(self.biziTpe_kuang)
        self.send_keys(self.biziTpe_kuang, Keys.DOWN)
        self.send_keys(self.bizeType_Xpath, Keys.ENTER)






