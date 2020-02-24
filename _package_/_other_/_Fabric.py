from fabric import Connection


# https://fabric-chs.readthedocs.io/zh_CN/chs/tutorial.html

def main():
    connect = Connection(host="192.168.0.99", port=22, user='root', connect_kwargs={"password": "jojo"})

    with connect.cd('/root/deployment/'):
        connect.run("ls -al")


if __name__ == '__main__':
    main()
