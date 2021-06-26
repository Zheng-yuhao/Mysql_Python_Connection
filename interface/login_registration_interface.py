"""
User's interface
"""
from db import models


def login_interface(user,pwd):
    obj = models.User(user,pwd)
    flag = obj.connect_mysql()
    if flag:
        return True, f'User[{user}] login successfully!'
    return False, f'Our database do not have the User[{user}'

def registration_interface(user,pwd):
    obj = models.User(user,pwd)
    flag = obj.insert_data()
    if flag:
        return True, f'[{user}]:Restoration successfully'
    else:
        return False, 'Error'