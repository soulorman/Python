#enconding: utf-8

'''
42.92.56.130 - - [23/Aug/2014:23:58:56 +0800] "GET /data/uploads/2013/0422/08/51748b0ef04e8.JPG HTTP/1.1" 200 \ "http://image.baidu.com/i?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&word=%E7%94%98%E8%82%83%E7%9C%81%E7%99%BD%E9%93%B6%E5%B8%82%E5%9B%BE%E7%89%87&step_word=&pn=414&spn=0&di=161249202510&rn=1&is=&istype=&ie=utf-8&oe=utf-8&in=2087&cl=2&lm=-1&st=&cs=4215836718%2C4107041133&os=281963354%2C3297720507&ln=1996&fr=&fmq=1408807884851_R&ic=&s=&se=&sme=0&tab=&width=&height=&face=&ist=&jit=&cg=&objurl=http%3A%2F%2Fwww.cihongcharity.org%2Fbbs%2FUploadFile%2F2013-8%2F201381518472144233.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B2zfpk_z%26e3Bv54AzdH3Fri5p5AzdH3F%25E0%25l9%25lb%25Eb%25bd%25bn%25E0%25lC%25b8%25E0%25ll%25BD%25El%25ln%25Bm%25Ec%25Bb%25bd%25E9%25BA%25BA%25E0%25A9%25BE%25Ec%25B8%25ba_z%26e3Bip4s" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"
'''

stats = {}
path = 'access.txt'

fhandler = open(path,'rt')
for line in fhandler:
    nodes = line.split()
    key = (nodes[0],nodes[6],nodes[8])
    stats[key] = stats.get(key,0) + 1
fhandler.close()

stats_list = list(stats.items())
for i in range(10):
    for i in range(len(stats_list) - 1):
        if stats_list[i][1] > stats_list[i + 1][1]:
            stats_list[i],stats_list[i+1] = stats_list[i+1] ,stats_list[i]
fhandler =  open('result.txt','wt')           
for k,v in stats_list[-1::-11]:
    print(k[0],k[1],k[2],v)
    fhandler.write('|{ip:10s}|{url:50s}|{code:5s}|{count:10d}|'.format(ip=k[0],url=k[1],code=k[2],count=v))

fhandler.close()