"""
The operation on database(Mysql)
"""
import pymysql

conn = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '',
        db = 'db666',
        charset = 'utf8',
        autocommit = True
    )


def check(user,pwd):
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = 'select * from userinfo where name=%s and password=%s'
    rows = cursor.execute(sql,(user,pwd))
    if rows:
        return True
    else:
        return False


def insert(user,pwd):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'insert into userinfo(name,password) values(%s,%s)'
    rows = cursor.execute(sql,(user,pwd))
    if rows:
        return True
    else:
        return False