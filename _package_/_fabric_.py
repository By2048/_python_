from fabric import Connection

from _._config_ import SSH_HOST, SSH_PORT, SSH_USER, SSH_RSA


# https://fabric-chs.readthedocs.io/zh_CN/chs/tutorial.html

def test():
    connect = Connection(
        host=SSH_HOST, port=SSH_PORT, user=SSH_USER,
        connect_kwargs={'key_filename': SSH_RSA}
    )

    with connect.cd('/root/'):
        connect.run("ls -al")


if __name__ == '__main__':
    test()
