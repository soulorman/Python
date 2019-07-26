# encoding:utf-8

stats = {}
path = 'access.txt'

fhandler = open(path)
for line in fhandler:
    nodes = line.split()
    key = (nodes[0],nodes[6],nodes[8])
    stats[key] = stats.get(key, 0) + 1
fhandler.close()

stats_list = list(stats.items())

for j in range(10):
    for i in range(len(stats_list) - 1):
        if stats_list[i][1] > stats_list[i+1][1]:
            stats_list[i],stats_list[i+1] = stats_list[i+1],stats_list[i]

print('{0:<18s}{1:<46s}{2:<7s}{3:<s}'.format('IP地址','访问目录','状态码','访问次数'))
for k,v in stats_list[:-11:-1]:
    print('{0:<20s}{1:<50s}{2:<10s}{3:<d}'.format(k[0],k[1],k[2],v))

