import pysnooper


@pysnooper.snoop()
def _and_():
    # 从左到右
    # 返回第一个False，
    # 无False返回最后一个
    _1 = 'a' and 'b'  # 'b'
    _2 = {} and 'b'  # {}
    _3 = 'a' and 'b' and 'c'  # 'c'


@pysnooper.snoop()
def _or_():
    # 从左到右
    # 返回第一个为True
    # 无True返回最后一个
    _1 = 'a' or 'b'  # 'a'
    _2 = '' or 'b'  # 'b'
    _3 = '' or [] or {}  # {}


@pysnooper.snoop()
def _and_or_():
    _1 = 1 and 'a' or 'b'  # 'a'
    _2 = 0 and 'a' or 'b'  # 'b'


assert False == 0
assert True == 1

if __name__ == '__main__':
    _and_()
    _or_()
    _and_or_()
