#enconding: utf-8
import traceback
from django.db import connection

class DBConnection(object):

    @staticmethod
    def execute_sql(sql,args=(),fetch=True,one=False):
        cnt,result = 0,None
        conn,cur = None,None
        try:
            cur = connection.cursor()
            cnt = cur.execute(sql,args)
            if fetch:
                result = cur.fetchone() if one else cur.fetchall()
            else:
                conn.commit()
        except BaseException  as e:
            print(e)
            print(traceback.format_exc())
        finally:
            if cur:
                cur.close()
                
        return cnt,result