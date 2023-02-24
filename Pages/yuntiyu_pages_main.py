from selenium.webdriver.common.by import By
from Base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class pageTwo(BasePage):
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)

    # 进入云体育后台
    def open_yuntiyu(self):
        self.get()

    # 学生人数
    def studentCount_verify(self):
       return self.element_get_text1(By.XPATH,"//*[@id=\"app\"]/div/section/main/div/h3")

    # 运功时长
    def sportTime_verify(self):
        return self.element_get_text1(By.XPATH,"//*[@id=\"app\"]/div/section/main/div/center/div[1]/div[1]/div/div/div[3]/div[2]/p")
    # 测试次数
    def testCount_verify(self):
        return self.element_get_text1(By.XPATH,"//*[@id=\"app\"]/div/section/main/div/center/div[1]/div[2]/div/div/div[3]/div[2]/p")