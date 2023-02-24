import os
from comm.read_conf import ReadConfig
# print(os.path.split(os.path.realpath(__file__)))
# print(os.path.split(os.path.realpath(__file__))[0])
#获取配置文件中的路径
project_conf_path=os.path.split(os.path.realpath(__file__))[0]+'\project.conf'
# print(project_conf_path)


#获取项目的路径
project_path=ReadConfig().read_config(project_conf_path,'PROJECT_PATH','project_path')
# print(project_path)



#print("testdata是：",test_data_path)




#http配置文件路径
http_conf_path=os.path.join(project_path,'conf','http.conf')
# print("http_conf_path是：",http_conf_path)

#数据库配置文件路径
datebae_conf_path=os.path.join(project_path,'conf','db.conf')
# print(datebae_conf_path)
#日志路径
log_path=os.path.join(project_path,'test_result','log','text_log.txt')
# print("log_path路径是;",log_path)
#测试报告的路径
http_report_path=os.path.join(project_path,'test_result','html')
# print("http_report路径是：",http_report_path)
#附件发送邮件的路径
email_path_html=os.path.join(project_path,'test_result','html','test2018-07-02_17_14_46.html')
email_path_log=os.path.join(project_path,'test_result','log','text_log.txt')




