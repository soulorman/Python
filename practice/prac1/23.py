#encoding: utf-8

tpl =
{
    host : {HOST};
    port : {PORT};
}

conf = tpl.format(HOST='1.1.1.1',PORT='8.8.8.8')

open('nginx.conf','wt').write(conf)