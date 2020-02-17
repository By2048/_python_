from _tool_._decorator_ import run_time

A = (i for i in range(1_000_000))
B = [i for i in range(1_000_000)]


@run_time
def test_a():
    data = sum(A)
    return data


@run_time
def test_b():
    data = sum(B)
    return data


@run_time
def test_c():
    data = sum(B)
    return data


if __name__ == '__main__':
    test_a()
    test_b()
    test_c()
