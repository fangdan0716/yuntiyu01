from selenium.webdriver.common.by import By
from Base.base_page import BasePage
class SearchOne(BasePage):
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)
    #进入百度
    def open_baidu(self):
        self.get()
    #输入数据
    def input_search_content(self,text):
        self.send_text(text,By.ID,"kw")
    # 点击按钮
    def click_baidu_search(self):
        self.left_click(By.ID, "su")
    def click_open_hao(self):
        self.left_click(By.XPATH,"//*[@id=\"1\"]/div/div[1]/h3/a")
