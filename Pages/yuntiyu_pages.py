from selenium.webdriver.common.by import By
from Base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class pagesOne(BasePage):
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)
    # 进入云体育后台
    def open_yuntiyu(self):
        self.get()
    # 切换登录方式
    # 密码登录
    def click_Login_password(self):
        self.left_click(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/ul/li[2]")
    # 手机号登录
    def click_Login_mobile(self):
        self.left_click(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/ul/li[1]")
    # 输入用户名
    def input_username_content(self,text):
        self.send_text(text,By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[1]/div/div/input")
    # 输入密码
    def input_password_content(self,text):
        self.send_text(text,By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/div/input")

    # 输入手机号
    def input_mobile_content(self, text):
        self.send_text(text, By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/div[1]/div/div/input")

    # 点击获取验证码
    def click_ckeckCode(self):
        self.single_click("//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/button/span")
    # 输入验证码
    def input_checkCode_content(self, text):
        self.send_text(text, By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/div/input")

    # 清空用户名
    def clear_username_content(self):
        self.clear_text(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/div[1]/div/div/input")

    # 清空密码
    def clear_password_content(self):
        self.clear_text(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/div/input")

    # 清空手机号
    def clear_mobile_content(self):
        self.clear_text(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/div[1]/div/div/input")
    #清空验证码
    def clear_checkCode_content(self):
        self.clear_text(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/div/input")

    # 点击登录按钮
    def click_login_button(self):
        self.left_click(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/button")

    # 点击登录按钮
    def click_login_button_is_enabled(self):
        return self.element_is_enable(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/form/button")
    # 手机号不正确：/html/body/div[2]/p
    # 手机号不正确：//*[@id="app"]/div/div[2]/div/form/div[1]/div/div[2]
    # 验证码不正确：/html/body/div[2]/p
    # 账号不存在：/html/body/div[2]/p
    # 密码错误： /html/body/div[2]/p
    def login_Error_info(self):
        # wait = WebDriverWait(self.driver, 20)
        # ele = self.driver.find_element(By.XPATH,"/html/body/div[2]/p")
        # wait.until(lambda x:ele.is_displayed())
        ele = self.driver.find_element(By.XPATH,"/html/body/div[2]/p")
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/p")))
        # 获取错误信息并返回
        return ele.get_attribute("textContent")
    def is_element_present(self,*locator):
        from selenium.common.exceptions import NoSuchElementException
        try:
            element = self.driver.find_element(*locator)
        except NoSuchElementException as e:
            # 打印异常信息
            print(e)
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True,element
