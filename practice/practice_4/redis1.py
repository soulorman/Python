# 连接redis

import redis

conn = redis.Redis(host='127.0.0.1', port=6379)
conn.set('x1','heelp')
val = conn.get('x1')

print(val)

