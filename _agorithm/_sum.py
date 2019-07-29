import time

A, B = (i for i in range(1_000_000)), [i for i in range(1_000_000)]


def time_function(function):
    def weapper():
        time_start = time.time()
        data = function()
        time_end = time.time()
        print(time_end - time_start, data)

    return weapper


def test_a():
    time_start = time.time()
    data = sum(A)
    time_end = time.time()
    print(time_end - time_start, data)


def test_b():
    time_start = time.time()
    data = sum(B)
    time_end = time.time()
    print(time_end - time_start, data)


@time_function
def test_c():
    data = sum(B)
    return data


if __name__ == '__main__':
    test_a()
    test_b()
    test_c()
