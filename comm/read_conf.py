import configparser
import time


class ReadConfig():
    def read_config(self,file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        value=cf.get(section,option)
        return value
if __name__ == '__main__':
    value=ReadConfig().read_config("../conf/http.conf","HTTP", 'ip')
    print(value)
    print(time.time())
