import os
import subprocess


def test_1():
    args = ['nslookup', 'www.baidu.com']
    result = subprocess.call(args)
    print(result)


def test_2():
    result = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in result.stdout.readlines():
        print(line)
    print('------------------------------')
    print(result.wait())


def test_3():
    output = os.popen('dir')
    print(output.read())

    tmps = os.popen('dir').readlines()
    for tmp in tmps:
        print(tmp, end='')


def test_4():
    data = subprocess.check_output('dir')
    print(data)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
