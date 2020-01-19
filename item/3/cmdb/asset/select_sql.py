# 查询sql
# encoding: utf-8

import MySQLdb

MYSQL_HOST = '192.168.31.102'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'No3fJQn66DZx'
MYSQL_DB = 'thorough_esd'
MYSQL_CHARSET = 'utf8'


# 今日上传数
SELECT_SQL_1 =  '''
                    select count(*) from upload_image where to_days(create_date) = to_days(now());
                '''

# 总上传数
SELECT_SQL_2 =  '''
                    select count(*) from  upload_image;
                '''

# 今日预测成功数
SELECT_SQL_3 =  '''
                    select count(*) from upload_image where status = 6 and to_days(create_date) = to_days(now());
                '''

# 总预测成功
SELECT_SQL_4 =  '''
                    select count(*) from upload_image where status = 6;
                '''

# 今日复原成功数
SELECT_SQL_5 =  '''
                    select count(*) from pathology_image where ai_predict_recover = 4 and to_days(create_date) = to_days(now());
                '''

# 总复原成功数
SELECT_SQL_6 =  '''
                    select count(*) from pathology_image where ai_predict_recover = 4;
                '''


def select():
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()

    result_1 = False
    result_2 = False
    result_3 = False
    result_4 = False
    result_5 = False
    result_6 = False

    try:
        cur.execute(SELECT_SQL_1)
        result_1 = cur.fetchall()[0][0]
    except BaseException as e:
        print(e)

    try:
        cur.execute(SELECT_SQL_2)
        result_2 = cur.fetchall()[0][0]
    except BaseException as e:
        print(e)

    try:
        cur.execute(SELECT_SQL_3)
        result_3 = cur.fetchall()[0][0]
    except BaseException as e:
        print(e)

    try:
        cur.execute(SELECT_SQL_4)
        result_4 = cur.fetchall()[0][0]
    except BaseException as e:
        print(e)

    try:
        cur.execute(SELECT_SQL_5)
        result_5 = cur.fetchall()[0][0]
    except BaseException as e:
        print(e)

    try:
        cur.execute(SELECT_SQL_6)
        result_6 = cur.fetchall()[0][0]
    except BaseException as e:
        print(e)

    cur.close()
    conn.close()

    return result_1, result_2, result_3, result_4, result_5, result_6