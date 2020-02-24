from _tool_._decorator_ import run_time

A = (i for i in range(1_000_000))
B = [i for i in range(1_000_000)]


@run_time
def test_a():
    return sum(A)


@run_time
def test_b():
    return sum(B)


@run_time
def test_c():
    return sum(B)


test_a()
test_b()
test_c()
