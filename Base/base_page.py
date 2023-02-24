from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import isDisplayed_js


class BasePage():
    """
    BasePage封装所有界面的公用方法。
    """
    # 实例化BasePage类时，事先执行的__init__方法，该方法需要传递参数
    def __init__(self,driver,url):
        self.driver = driver
        self.base_url = url
    # 进入网址
    def get(self):
        self.driver.get(self.base_url)
    # 元素定位
    def get_element(self,*locator):
        return self.driver.find_element(*locator)
    # 点击
    def left_click(self,*locator):
        ActionChains(self.driver).click(self.get_element(*locator)).perform()

        # 点击
    def single_click(self, *locator):
        self.driver.find_element(*locator).click()
    # 输入
    def send_text(self , text , *locator):
        self.driver.find_element(*locator).send_keys(text)

    # 清除
    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()

    # 表单切换
    def switch_iframe(self, *locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))

    # 表单切换
    def switch_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])
    # # 判断元素是否显示
    # def is_displayed(self):
    #     """Whether the element is visible to a user."""
    #     # Only go into this conditional for browsers that don't use the atom themselves
    #     if self._w3c:
    #         return self.parent.execute_script(
    #             "return (%s).apply(null, arguments);" % isDisplayed_js,
    #             self)
    #     else:
    #         return self._execute(Command.IS_ELEMENT_DISPLAYED)['value']

    # 判断元素是否显示
    def element_is_displayed(self, *locator):
        return self.driver.find_element(*locator).is_displayed()
    # 获取元素属性值
    def element_get_attribute(self,value, *locator):
        return self.driver.find_element(*locator).getAttribute(value)

    # 获取元素的文本值
    def element_get_text(self,  *locator):
        return self.driver.find_element(*locator).getText()

    def element_get_text1(self,  *locator):
        return self.driver.find_element(*locator).get_attribute("textContent")
    def element_get_text2(self,  *locator):
        return self.driver.find_element(*locator).text
    # 获取元素的标签名
    def elements_get_tagName(self,  *locator):
        return self.driver.find_element(*locator).getTagName()

# 判断元素是否可用
    def element_is_enable(self,  *locator):
        return self.driver.find_element(*locator).is_enabled()