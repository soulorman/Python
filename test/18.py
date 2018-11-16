#encoding: utf-8

tpl = open('/tmp/ngx.conf','rt').read()

conf = tpl.format(HOST='1.1.1.1',PORT='88')

open('/tmp/ngx1.conf','wt').write(conf)
