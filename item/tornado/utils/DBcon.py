import pymysql
import traceback

class DBconnction(object):
    
    @classmethod
    def execute_mysql(cls, sql, args=(), fetch=True, one=False):
        result = None
        cur, conn = None, None
        try:
            conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
            cur = conn.cursor()
            cur.execute(sql, args)
            if fetch:
                result = cur.fetchall() if one else cur.fetchone()
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

        return result