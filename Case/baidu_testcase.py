import unittest
from selenium import webdriver
from Pages.search_pages import SearchOne
class BaiBu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver107.62.exe")
        cls.driver.implicitly_wait(10)
    def test001(self):
        url="http://www.baidu.com"
        s = SearchOne(self.driver,url)
        s.open_baidu()
        s.input_search_content("123")
        s.click_baidu_search()
        s.click_open_hao()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def tearDown(self) -> None:
    #      self.driver.quit()
        pass
if __name__ == '__main__':
    unittest.main()

