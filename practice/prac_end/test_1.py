import MySQLdb

MYSQL_HOST = '192.168.31.103'
MYSQL_PORT = 13306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'file_test'
MYSQL_CHARSET = 'utf8'

SELECT_SQL =    '''
                    SELECT dir 
                    FROM dir
                    LIMIT 10
                '''

conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
cur = conn.cursor()


cur.execute(SELECT_SQL)
print(cur.fetchall())
#result = cur.fetchall()
        
cur.close()
conn.close()
 
