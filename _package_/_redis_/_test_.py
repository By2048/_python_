import redis

db = redis.Redis(connection_pool=redis_conn_pool)
keys = db.scan_iter(match='product*')
print(keys)
print(list(keys))

data = db.scan(match='product*')


def test_set():
    data = {
        'name-test-1': {'data': True},
        'name-test-2': {'data': 1},
        'name-test-3': {'data': 123}
    }
    for key in list(data):
        data[key] = json.dumps(data[key], ensure_ascii=False)

    db = redis.Redis(connection_pool=redis_conn_pool)
    r = db.mset(data)
    print(r)


def test_get():
    db = redis.Redis(connection_pool=redis_conn_pool)
    keys = db.scan_iter(match=f'name-test-*', count=REDIS_DB_SIZE)
    _keys_ = db.scan_iter(match=f'name-test-*', count=REDIS_DB_SIZE)
    data = {}
    for key in _keys_:
        data[key] = None

    keys = list(keys)

    values = db.mget(keys)
    for key, value in zip(list(data), values):
        value = json.loads(value)
        data[key] = value

    print(data)


if __name__ == '__main__':
    pass
    init_device_online()
    # test_get()
