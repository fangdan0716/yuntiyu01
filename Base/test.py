import time

# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver107.62.exe")
# driver.get("http://yuntiyu-test.dream-sports.cn/#/login?redirect=%2FtestRecords")
# driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/ul/li[2]").click()
# driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[1]/div/div/input").send_keys("yunnan112")
# driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/div[2]/div/div/input").send_keys("dabai521")
# driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/button").click()
# #driver.find_element(By.XPATH,"/html/body/div[2]/p").is_displayed()
# a = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/ul/li[2]").get_attribute("role")
# b = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/form/ul/li[2]").get_attribute("textContent")
# print(a,b)


text ="学生人数 5771人"

print(text.split())
print(text.split()[1][0:-1])