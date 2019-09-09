1、先创建数据库

CREATE DATABASE file_test default charset utf8;
use file_test;
CREATE TABLE file(
    id int not null primary key auto_increment comment 'id',
    file_name varchar(128) not null default '' comment '文件名',
    file_path varchar(512) not null  comment '文件路径',
    status int not null default 1 comment '文件状态: 1代表文件正常, 0代表文件有问题',
    is_cancer bool not null default false comment '是否有癌症，1表示有, 0表示没有',
    created_time datetime,
    unique key file_name (file_name, file_path)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


2、写python文件

#encoding: utf-8

import re
import os
import MySQLdb
from datetime import datetime

# 
SELECT_SQL =    '''
                    SELECT dir //目录所在字段名
                    FROM dir; //目录所在表名字
                '''


INSERT_SQL =    '''
                    INSERT INTO file(file_name, file_path, created_time)
                    VALUES(%s, %s, %s);
                '''

pattern = r'.*\.(kfb|tif|tiff|tmap|svs|bif|dmetrix|KFB|TIF|TIFF|TMAP|SVS|BIF|DMETRIX)$'


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
    conn = MySQLdb.connect(host="192.168.31.103", port=13306, user="root", passwd="123456", db="file_test", charset='utf8')
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


if __name__ == '__main__':
    conn = MySQLdb.connect(host="192.168.31.103", port=13306, user="root", passwd="123456", db="file_test", charset='utf8')
    cur = conn.cursor()

    try:
        cur.execute(SELECT_SQL)
        result = cur.fetchall()

    except BaseException as e:
        pass

    cur.close()
    conn.close()

    file_list = []    
    for dir in result:
        isDir(file_list, dir[0])

    ok_count, error_count, errors = putDB(file_list)
    print("成功次数 : ", ok_count)
    print("失败次数 : ", error_count)
    if error_count != 0:
        print("失败的文件为：", errors)
