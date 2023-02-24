# 主页
import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.yuntiyu_pages import pagesOne
from Pages.yuntiyu_pages_main import pageTwo

from selenium.webdriver.support import expected_conditions as EC

from comm.do_mysql import DbInfo
from conf import project_path
from comm.read_conf import ReadConfig

class yunMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="C:\Program Files\Google\Chrome\Application\chromedriver107.62.exe")
        cls.driver.implicitly_wait(10)
    def setUp(self) -> None:
        url = "http://yuntiyu-test.dream-sports.cn/#/login?redirect=%2FtestRecords"
        self.username = 'yunnan1'
        self.s = pagesOne(self.driver, url)
        self.s.open_yuntiyu()
        self.s.click_Login_password()
        self.s.clear_username_content()
        self.s.input_username_content(self.username)
        self.s.clear_password_content()
        self.s.input_password_content("dabai521")
        self.s.click_login_button()


    """学校总人数"""
    def test001(self):
        url = "http://yuntiyu-test.dream-sports.cn/#/testPlan/detail?id=1583379209719484428&name=%E4%BA%91%E5%8D%97%E7%9C%81%E5%88%9D%E4%B8%AD%E5%AD%A6%E7%94%9F%E4%BD%93%E8%82%B2%E8%80%83%E8%AF%95&testType=1&term=1&grade=9&gradeId=11234&studentCount=32&clazzIds=11269&hasTest=2&testDates=%5Bobject%20Object%5D&gradeName=%E4%B9%9D%E5%B9%B4%E7%BA%A7&status=%E5%B7%B2%E7%BB%93%E6%9D%9F&schoolYear=685"
        self.m = pageTwo(self.driver, url)
        time.sleep(1)
        # text = self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/section/main/div/h3").get_attribute("textContent")
        # 页面中获取到的学校人数
        text = self.m.studentCount_verify()

        # 分割并截取页面中学生人数
        actuallyStudentsCount = text.split()[1][0:-1]
        # 获取数据库配置
        config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
        # 连接数据库
        sql_conn = DbInfo(config)
        # 查询语句
        excectStudentCountSQL ="SELECT COUNT(*) FROM isport_dev.t_tester t WHERE t.`enable`=1 AND user_id = (SELECT id FROM t_user u WHERE u.username='"+self.username+"') AND t.school_year = (SELECT id FROM t_school_year t where t.school_id =(SELECT organizes_id FROM t_user u  WHERE u.username='"+self.username+"' )AND t.current_flag=1);"
        # 执行语句并获取到学生总人数
        excectStudentCount = str(sql_conn.get_data(excectStudentCountSQL, 1)[0][0])
        if(actuallyStudentsCount== excectStudentCount):
            print("该学校学生人数显示正确")
        else:
            print("请检查改学校学生人数")

    """运动时长"""
    def test002(self):
        """SELECT SUM(r.test_duration) FROM t_exercise_result r
        WHERE r.user_id =(SELECT id FROM t_user u WHERE u.username='yunnan1')
        AND r.`enable`=1
        AND r.tester_id in (SELECT id FROM t_tester WHERE user_id =441 AND `enable`=1);"""



    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(yunMain("test001"))

    run = unittest.TextTestRunner()
    run.run()
