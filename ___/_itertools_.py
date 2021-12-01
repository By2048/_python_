from itertools import chain


def test_1():
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']

    print(chain(a, b))

    for c in chain(a, b):
        print(c)


def test_2():
    a = [1, 2, 3, 4]
    b = ('x', 'y', 'z')

    print(chain(a, b))

    for c in chain(a, b):
        print(c)


if __name__ == '__main__':
    test_1()
    test_2()
