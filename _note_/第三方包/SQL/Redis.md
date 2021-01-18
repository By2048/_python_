
```py
import redis
import time

redis_server = redis.Redis(host='127.0.0.1', port=6379)
redis_server.set('a', '1111111')
item = redis_server.get('a')
print(item)

redis_server.expire('a', 3)
# 设置过期时间为3秒

```