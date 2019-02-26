#encoding: utf-8
stats = {}
path = '/tmp/access.log'

fhandler = open(path)
for line in fhandler:
    nodes = line.split()
    key = (nodes[0],nodes[6],nodes[8])
    stats[key] = stats.get(key,0) + 1
fhandler.close()

stats_list = list(stats.items())
for j in range(10):
    for i in range(len(stats_list) - 1):
        if stats_list[i][1] > stats_list[i+1][1]:
            stats_list[i],stats_list[i+1] = stats_list[i+1],stats_list[i]
f = open('result','wt')
f.write('{ip:20s}{uri:20s}{code:5s}{count:>10s}\n'.format(ip='IP',uri='URI',code='CODE',count='TONGJI'))
for key,value in stats_list[-1:-11:-1]:
    f.write('{ip:20s}{uri:20s}{code:5s}{count:10d}\n'.format(ip=key[0],uri=key[1],code=key[2],count=value))

f.close()
