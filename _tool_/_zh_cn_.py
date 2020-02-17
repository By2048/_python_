import string


def is_zh_cn(item):
    return '\u4e00' <= item <= '\u9fff'


def is_zh_code(item):
    return item in "└＾＜｜〛＼〾〝〃＇＋〜＃〚〿“「、‘＄）【＆】；％＝’…｛｀｠〘﹏｟。＠〔" \
                   "［，－╚／？＞｝〟〰《–—」〙〕］（”〈〉』！·〞『：＂＿〗┐～╗〖》＊↓↑←→"


def is_en(item):
    return item in string.ascii_letters + '1234567890'


def get_length(data):
    num = 0
    for item in data:
        if is_zh_cn(item) or is_zh_code(item):
            num += 2
            continue
        if is_en(item):
            num += 1
            continue
        print(item)
    return num
