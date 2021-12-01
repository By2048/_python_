import os


def test_1():
    """
    65001   UTF-8
    936     GBK
    """

    os.system('dir')
    os.system('chcp 65001')
    os.system('dir')


if __name__ == '__main__':
    test_1()
