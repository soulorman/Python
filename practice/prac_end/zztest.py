#encoding: utf-8

import re
import os
import MySQLdb
from datetime import datetime
 
SELECT_SQL =    '''
                    SELECT dir
                    FROM dir; 
                '''


INSERT_SQL =    '''
                    INSERT INTO file(file_name, file_path, created_time)
                    VALUES(%s, %s, %s);
                '''

pattern = r'.*\.(kfb|tif|tiff|tmap|svs|bif|dmetrix|KFB|TIF|TIFF|TMAP|SVS|BIF|DMETRIX)$'

MYSQL_HOST = '192.168.31.103'
MYSQL_PORT = 13306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'file_test'
MYSQL_CHARSET = 'utf8'


# 递归去收集文件名
def isDir(file_list, dir):
    for file in os.listdir(dir):
        if os.path.isdir(dir + '/' + file):
            isDir(file_list, dir + '/' + file)
        else:
            try:
                result = re.match(pattern, file)
                file_list.append((result.group(), dir))
            except BaseException as e:
                pass

    return file_list


def putDB(file_list):
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()

    ok_count, error_count = 0, 0
    errors = []

    for tup in file_list:
        try:
            cur.execute(INSERT_SQL, (tup[0], tup[1], datetime.now()))
            if ok_count % 5000 == 0:
                conn.commit()
            
            ok_count += 1
        except BaseException as e:
            error_count += 1
            errors.append((tup[0], tup[1]))

    conn.commit()
    cur.close()
    conn.close()

    return ok_count, error_count, errors


def read_dir():
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()

    try:
        cur.execute(SELECT_SQL)
        result = cur.fetchall()
        
    except BaseException as e:
        pass
    cur.close()
    conn.close()
    
    return result

def main():
    dir_result = read_dir()

    file_list = []   
    for dir in dir_result:
        try:
            isDir(file_list, dir[0])
        except BaseException as e:
            print(e)

    ok_count, error_count, errors = putDB(file_list)
    print("成功次数 : ", ok_count)
    print("失败次数 : ", error_count)
    if error_count != 0:
        print("失败的文件为：", errors)


if __name__ == '__main__':
    main()
