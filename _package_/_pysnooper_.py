import numpy
import pysnooper


@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


def large(l):
    return isinstance(l, list) and len(l) > 5


def print_list_size(l):
    return 'list(size={})'.format(len(l))


def print_ndarray(a):
    return 'ndarray(shape={}, dtype={})'.format(a.shape, a.dtype)


@pysnooper.snoop(custom_repr=((large, print_list_size), (numpy.ndarray, print_ndarray)))
def sum_to_x(x):
    l = list(range(x))
    a = numpy.zeros((10, 10))

    return sum(l)


if __name__ == '__main__':
    number_to_bits(6)

    print('-------------------------')

    sum_to_x(10000)
