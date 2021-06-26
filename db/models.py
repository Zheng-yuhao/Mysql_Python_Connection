"""
Creating classes to attribute functions
"""
from db import common

class User():
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

    def connect_mysql(self):
        flag = common.check(self.user,self.pwd)
        if flag:
            return True
        else:
            return False

    def insert_data(self):
        flag = common.insert(self.user,self.pwd)
        if flag:
            return True
        else:
            return False
