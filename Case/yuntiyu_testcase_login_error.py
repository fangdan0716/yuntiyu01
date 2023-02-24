import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.yuntiyu_pages import pagesOne
from selenium.webdriver.support import expected_conditions as EC

from comm.do_mysql import DbInfo
from conf import project_path
from comm.read_conf import ReadConfig

class yuntiyu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver107.62.exe")
        cls.driver.implicitly_wait(10)

    def setUp(self) -> None:
        url = "http://yuntiyu-test.dream-sports.cn/#/login?redirect=%2FtestRecords"
        self.s = pagesOne(self.driver, url)
        self.s.open_yuntiyu()
    """密码登录：密码错误"""
    def test001(self):
        self.s.click_Login_password()
        self.s.input_username_content("yunnan1")
        self.s.input_password_content("dabai521121")
        self.s.click_login_button()
        error_message = self.s.login_Error_info()
        #print(error_message)
        if(error_message ==u'密码错误！'):
            print("密码错误")
        else:
            print("---用例失败-----")
    """密码登录：用户名不存在"""
    def test002(self):
        self.s.click_Login_password()
        self.s.input_username_content("yunnan1232")
        self.s.input_password_content("dabai521")
        self.s.click_login_button()
        error_message = self.s.login_Error_info()
        #print(error_message)
        #self.assertEqual(error_message,u'用户账号不存在！',"用户名不存在")
        if(error_message ==u'用户账号不存在！'):
            print("用户名不存在")
        else:
            print("用例失败")

    """密码登录：密码为空不可点击"""
    def test003(self):
        self.s.click_Login_password()
        self.s.input_username_content("yunnan1232")
        #print(s.click_login_button_is_enabled())
        if(self.s.click_login_button_is_enabled() == False):
            print("密码为空不可点击")
        else:
            print("当前用户密码为空登录按钮应该不可点击")
    """密码登录：用户名为空不可点击"""
    def test004(self):
        self.s.click_Login_password()
        self.s.input_password_content("dabai521")
        #print(s.click_login_button_is_enabled())
        if(self.s.click_login_button_is_enabled() == False):
            print("用户名为空不可点击")
        else:
            print("当前用户为空登录按钮应该不可点击")

    """手机号登录：手机号为空，验证码为空"""
    def test005(self):
        self.s.click_Login_mobile()
        if (self.s.click_login_button_is_enabled() == False):
            print("手机号和验证码为空，登录按钮不可点击")
        else:
            print("手机号和证码为空，登录按钮应该不可点击，请检查逻辑是否正确")

    """手机号登录：手机号为空"""
    def test006(self):
        #点击手机号登录
        self.s.click_Login_mobile()
        self.s.clear_mobile_content()
        self.s.input_mobile_content("")
        self.s.input_checkCode_content("321123")
        if (self.s.click_login_button_is_enabled() == False):
            print("手机号为空，登录按钮不可点击")
        else:
            print("手机号为空，登录按钮应该不可点击，请检查逻辑是否正确")

    """手机号登录：验证码为空"""
    def test007(self):
        self.s.click_Login_mobile()
        self.s.input_mobile_content("18112344321")
        self.s.clear_checkCode_content()
        self.s.input_checkCode_content("")
        if (self.s.click_login_button_is_enabled() == False):
            print("验证码为空，登录按钮不可点击")
        else:
            print("验证码为空，登录按钮应该不可点击，请检查逻辑是否正确")

    """手机号登录：手机号正常，验证码错误"""
    def test008(self):
        self.s.click_Login_mobile()
        self.s.input_mobile_content("18112344321")
        self.s.clear_checkCode_content()
        self.s.input_checkCode_content("123123")
        self.s.click_login_button()
        error_message = self.s.login_Error_info()
        if (error_message == "请输入正确的验证码！"):
            print("验证码校验正确，")
        else:
            print("验证码校验错误")


    """手机号登录：手机号错误"""
    def test009(self):
        self.s.click_Login_mobile()
        self.s.input_mobile_content("124321")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/button/span").click()
        error_message = self.s.login_Error_info()
        if (error_message == "请输入正确的手机号码！"):
            print("手机号校验正确，")
        else:
            print("手机号校验错误")

    # 手机号用户不存在！短信发送失败，请稍后再试
    def test0010(self):
        #手机号
        mobile = '14101011212'
        #self.s.click_Login_mobile()
        self.s.input_mobile_content(mobile)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/button/span").click()
        if(self.s.login_Error_info() != "短信发送失败，请稍后再试"):
            time.sleep(3)
            config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
            sql_conn = DbInfo(config)
            sql_1 = 'select code from isport_dev.t_sms_log s where s.mobile ="' + mobile + '"order by s.id desc limit  1 ; '
            check_code = sql_conn.get_data(sql_1,1)[0][0]
            time.sleep(3)
            self.s.input_checkCode_content(check_code)
            self.s.click_login_button()
            time.sleep(1)
            error_message = self.s.login_Error_info()
            if (error_message == "手机号用户不存在！"):
                print("请确认并请检查手机号，")
            else:
                print("手机号校验错误")
        else:
            print("当前手机号短信发送失败")


    """密码登录且用户名密码正确"""
    def test0011(self):
        self.s.click_Login_password()
        self.s.clear_username_content()
        self.s.input_username_content("yunnan1")
        self.s.clear_password_content()
        self.s.input_password_content("dabai521")
        self.s.click_login_button()
        time.sleep(1)
        try:
            locator = (By.XPATH,"//*[@id=\"app\"]/div/section/main/div/h1")
            ele = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            login_info_actual = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/section/main/div/h1").get_attribute("textContent")
            login_info_expect = u"云南师范中学1中"
            if (login_info_expect == login_info_actual):
                print("当前用户登录成功")
                self.driver.maximize_window()
                self.driver.implicitly_wait(3)
                self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/section/header/div/div/div[2]/div").click()
                time.sleep(5)
                # /html/body/ul/li[2]

                logout_locator =(By.XPATH,"/html/body/ul/li[2]")
                logout_ele = WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(logout_locator))
                self.driver.find_element(By.XPATH,"/html/body/ul/li[2]").click()
                print("退出登录成功")
                time.sleep(2)
            else:
                print("当前用户登录失败，请检查登录信息是否正确")
        except NoSuchElementException as e:
            print("ele can't find")
            print(e)

    """手机验证码发送失败"""
    def test0012(self):
        #手机号
        mobile = '14514514522'
        #self.s.click_Login_mobile()
        self.s.input_mobile_content(mobile)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/button/span").click()
        #send_message_fail = self.s.login_Error_info()
        #if (send_message_fail != "短信发送失败，请稍后再试"):
        #else:
        #    print("当前登录的手机号短信发送失败")
        time.sleep(3)
        config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
        sql_conn = DbInfo(config)
        sql_1 = 'select code from isport_dev.t_sms_log s where s.mobile ="' + mobile + '"order by s.id desc limit  1 ; '
        check_code = sql_conn.get_data(sql_1, 1)[0][0]
        print(check_code)
        time.sleep(3)
        self.s.input_checkCode_content(check_code)
        self.s.click_login_button()
        time.sleep(1)
        try:
            locator = (By.XPATH, "//*[@id=\"app\"]/div/section/main/div/h1")
            ele = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            login_info_actual = self.driver.find_element(By.XPATH,
                                                         "//*[@id=\"app\"]/div/section/main/div/h1").get_attribute(
                "textContent")
            sql_2 = "select o.organizes_name from isport_dev.t_organizes o where  o.id = (select u.organizes_id from  isport_dev.t_user u where u.id = (select s.user_id from  isport_dev.t_sms_log s where s.mobile = '" + mobile + "' limit 1));"
            sql_result = sql_conn.get_data(sql_2, 1)[0][0]
            if(sql_result[0]) is not None:
                login_info_expect = sql_result
                if (login_info_expect == login_info_actual):
                    print("当前用户登录成功")
                    self.driver.find_element(By.XPATH,
                                             "//*[@id=\"app\"]/div/section/header/div/div/div[2]/div/span/svg/use").click()
                    self.driver.find_element(By.XPATH, "/html/body/ul/li[2]").click()
                    print("登录成功")
                    time.sleep(2)
                else:
                    print("当前用户登录失败，请检查登录信息是否正确")
            else:
                print("数据库中未查询到对于手机号的验证码")
        except NoSuchElementException as e:
            print("ele can't find")
            print(e)


    def tearDown(self) -> None:
          #self.driver.quit()
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(yuntiyu("test0011"))
    run = unittest.TextTestRunner()
    run.run(suite)
    #unittest.main()

