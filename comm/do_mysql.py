import mysql.connector

class DbInfo:
    def __init__(self,config):
        self.config=config

    def get_data(self,sql,state):
        cnn= mysql.connector.connect(**self.config)

        if state==1:
            cursor=cnn.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
        elif state==2:
            cursor = cnn.cursor()
            cursor.execute(sql)
            cursor.execute('commit')
            result=[]
        cursor.close()
        cnn.close()
        return result



if __name__ == '__main__':
    from conf import project_path
    from comm.read_conf import ReadConfig
    config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
    print(config)
    t=DbInfo(config)
    mobile ='18302123929'
    sql_2 ="select o.organizes_name from isport_dev.t_organizes o where  o.id = (select u.organizes_id from  isport_dev.t_user u where u.id = (select s.user_id from  isport_dev.t_sms_log s where s.mobile = '"+mobile+"' limit 1));"
    res=t.get_data(sql_2,1)
    print(res)

