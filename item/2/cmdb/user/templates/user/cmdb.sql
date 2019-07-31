create database cmdb_test default charset utf8;

use cmdb_test;

create table user(
    id int primary key auto_increment,
    name varchar(32) not null default '',
    age int not null default 0,
    sex bool not null default 1,
    tel varchar(32) not null default '',
    birthday date not null,
    password varchar(512) not null default ''
) default charset utf8;

insert into user(name,age,sex,tel,birthday,password)
    values
    ('kk', 15, 1, '123456', '1980-10-10', '123'),
    ('kk1', 30, 1, '13x', '1921-10-10', '13'),
    ('kk2', 1, 0, '12x', '2001-10-10', '1232'),
    ('kk3',100, 1, '13x', '1996-10-10', '1231'),
    ('kk4', 22, 0, '13x', '1990-10-10', '1232');