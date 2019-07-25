# encoding: utf-8
path = 'ngx.tpl'
path1 = 'ngx.conf'

tpl = open(path).read()

conf = tpl.format(host='1.1.1.1',port=80)

open(path1,'wt').write(conf)
