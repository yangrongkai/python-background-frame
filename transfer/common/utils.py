# coding=UTF-8

'''
Created on 2016年8月6日

@author: Administrator
'''

# import python standard package

# import thread package

# import my project package
import os
import pymysql
import urllib.request
import datetime

from tuoen.middleware.oss import oss_helper

init_dir = os.path.dirname((os.path.abspath(__file__)))
db_file_dir = os.path.join(init_dir,'db')

class FileManager(object):
    
    @classmethod
    def read_file(cls, file_name):
        abs_path = os.path.join(db_file_dir, file_name)
        line_list = []
        with open(abs_path,'rb') as f :
            for line in f.readlines():
                line = line.decode().strip()
                line_list.append(line)
        return line_list

class DBConnect(object):
    
    def __init__(self, user, passwd, host, db, port = 3306, charset = 'utf8'):
        self.host = host
        self.passwd = passwd
        self.user = user
        self.port = port 
        self.db = db
        self.charset = charset

    def execute(self, sql):
        try:
            connection = pymysql.connect(host = self.host, password = self.passwd, \
                user = self.user, port = self.port, db = self.db, charset = self.charset)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                cursor.execute(sql)
                # 获取查询结果
                result = cursor.fetchall()
                return result
        finally:
            connection.close();
            
class FileThansfer(object):
    
    def __init__(self):
        self.http_head = "http://123.56.198.183/resources/"
    
    def thansfer(self, url, store_module):
        request_url = self.http_head + urllib.request.quote(url)
        store_name = url.split("/")[-1]
        with urllib.request.urlopen(request_url) as response:
            content = response.read()
            return oss_helper.put_object_byIO(store_name, content, store_module)
        

class HelperTransfer(object):

    @classmethod
    def get_print_message(cls, message):
        return "[{cur_time}] {message}".format(message = message, cur_time = datetime.datetime.now())
        