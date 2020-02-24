import os
import json
import functools
import time

from kazoo.client import KazooClient


def run_time(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = function(*args, **kwargs)
        time_end = time.time()
        print(f"name:{function.__name__}    time:{time_end - time_start}")
        return result

    return wrapper


# @zk.add_listener
# def listener(state):
#     print(f"state:{state}")
#     if state == KazooState.CONNECTED:
#         if zk.client_state == KeeperState.CONNECTED_RO:
#             print("Read only mode!")
#         else:
#             print("Read/Write mode!")


@run_time
def get_data():
    path = os.path.abspath(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path = os.path.join(path, 'file', 'device.json')
    with open(path) as file:
        data = file.read()
    data = json.loads(data)
    data = json.dumps(data)
    data = data.encode()
    return data


@run_time
def main():
    data = get_data()

    zk = KazooClient('s50.53iq.com:21811,s50.53iq.com:21812,s50.53iq.com:21813')
    zk.start()

    for i in range(999):
        path = f'/device/{i}'
        print(path)
        if not zk.exists(path):
            zk.create(path, data, makepath=True)

    zk.create('/test', b'test1234', makepath=True, ephemeral=True)

    # if zk.exists(path):
    #     zk.delete(path)

    # path = f'/device/{1}'
    # if zk.exists(path):
    #     data, status = zk.get(path)
    #     print(1, data, status, sep='\n')

    children = zk.get_children(f'/device/')
    print(children)

    zk.get_children_async()

    zk.stop()
    zk.close()


@run_time
def version():
    zk = KazooClient('s50.53iq.com:21811,s50.53iq.com:21812,s50.53iq.com:21813')
    zk.start()

    data = zk.server_version()
    print(data)

    zk.stop()
    zk.close()


@run_time
def clear():
    zk = KazooClient('s50.53iq.com:21811,s50.53iq.com:21812,s50.53iq.com:21813')
    zk.start()

    data = zk.delete(f'/device', recursive=True)
    print(data)

    zk.stop()
    zk.close()


if __name__ == '__main__':
    # main()
    version()
    # clear()
