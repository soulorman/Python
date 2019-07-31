# encoding: utf-8
import traceback
import MySQLdb

MYSQL_HOST = '192.168.31.103'
MYSQL_PORT = 13306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'cmdb'
MYSQL_CHARSET = 'utf8'

def execute_mysql(sql, args=(), fetch=True, one=False):
    cnt, result = 0, None
    conn, cur = None, None
    try:
        conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
        cur = conn.cursor()
        cur.execute(sql, args)
        if fetch:
            result = cur.fetchone() if one else cur.fetchall()
        else:
            conn.commit()
    except BaseException as e:
        print(e)
        print(traceback.format_exc())
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    return cnt, result