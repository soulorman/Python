import pymysql
from datetime import datetime

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'cmdb'
MYSQL_CHARSET = 'utf8'

SELECT_SQL = '''
                SELECT name, password 
                FROM userinfo
                WHERE id = %s
            '''
INSERT_SQL = '''
                INSERT INTO userinfo(name, time)
                VALUES (%s, %s)
             '''


conn = pymysql.connect(
                        host = MYSQL_HOST,
                        port = MYSQL_PORT,
                        user = MYSQL_USER,
                        password = MYSQL_PASSWORD,
                        db = MYSQL_DB,
                        charset = MYSQL_CHARSET
                        )

cur = conn.cursor()


#cur.execute(SELECT_SQL,(1,))
try:
    cur.execute(INSERT_SQL,(datetime.now()))
    conn.commit()
except:
    conn.rollback()

#result = cur.fetchall()
#result = cur.fetchone()
#print(result)
cur.close()
conn.close()

#print('name:{}'.format(result[0][1]))
#print('password:{}'.format(result[0][2]))
#print('info:{}'.format(result[0][3]))
#print('时间是:{}'.format(result[0][4].strftime('%Y-%m-%d %X')))