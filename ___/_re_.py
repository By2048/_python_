import re

from _tool_._other_ import run_all_test, print_value


def test_1():
    item_1 = re.split(r"\W+", "aaa, bbb, ccc")
    item_3 = re.split(r"\W+", "aaa, bbb, ccc", 1)
    item_2 = re.split(r"(\W+)", "aaa, bbb, ccc")
    item_4 = re.split(r'\W+', 'hello world')
    print_value(locals())


def test_2():
    file = """
    -- start sql config --
    host="1.1.1.1"
    pwd="111"
    -- end sql config --
    """
    rule = "(-- start {0} config --)([\s\S]+)(-- end {0} config --)".format("sql")
    item_1 = re.search(rule, file, re.M).groups()
    item_2 = re.sub(rule, "[NO]", file, re.M).strip()
    print_value(locals())


def test_3():
    rule_1 = r"(Screenshot_)(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(.png)"
    rule_2 = r"\2-\3-\4 \5-\6-\7\8"
    name_old = "Screenshot_20210318215042.png"
    name_new = re.sub(rule_1, rule_2, name_old)
    print_value(locals())


def test_4():
    item_1 = re.findall(r"\d", "aaa bbb 111 222")
    item_2 = re.compile(r"\d{1,4}")
    item_3 = item_2.findall("aaa bbb 111 222")

    item_4 = re.match(r"[1-3]", "aaa bbb 111 222")
    item_4_1 = re.match(r"[a-c]", "aaa bbb 111 222")
    item_4_2 = re.fullmatch(r"[1-3]", "aaa bbb 111 222")
    item_4_3 = re.fullmatch(r"[a-c]{3} [a-c]{3} \d+ \d+", "aaa bbb 111 222")

    item_6 = re.findall(r"[1-3]", "aaa bbb 111 222")
    item_7 = re.search(r"[1-3]", "aaa bbb 111 222")
    item_7_1 = re.search(r"[1-3]", "aaa bbb 111 222").span()
    print_value(locals())


if __name__ == '__main__':
    run_all_test(globals())

    # re.I 忽略大小写
    # re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
    # re.M 多行模式
    # re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
    # re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
    # re.X 为了增加可读性，忽略空格和 # 后面的注释
