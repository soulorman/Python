# encoding: utf-8
import traceback
from django.db import connection

class DBconnection(object):
    
    @classmethod
    def execute_mysql(cls, sql, args=(), fetch=True, one=False):
        cnt, result = 0, None
        cur = None, None
        try:
            cur = connection.cursor()
            cur.execute(sql, args)
            if fetch:
                result = cur.fetchone() if one else cur.fetchall()
            else:
                connection.commit()
        except BaseException as e:
            print(e)
            print(traceback.format_exc())
        finally:
            if cur:
                cur.close()
            if connection:
                connection.close()

        return cnt, result