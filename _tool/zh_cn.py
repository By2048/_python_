def is_zh_cn(letter):
    if '\u4e00' <= letter <= '\u9fff':
        return True
    else:
        return False


def is_zh_code(symbol):
    codes = "└＾＜｜〛＼〾〝〃＇＋〜＃〚〿“「、‘＄）【＆】；％＝’…｛｀｠〘﹏｟。＠〔［，－╚／？＞｝〟〰《–—」〙〕］（”〈〉』！·〞『：＂＿〗┐～╗〖》＊↓↑←→"
    if symbol in codes:
        return True
    else:
        return False


def get_zh_cn_num(word):
    num = 0
    for letter in word:
        if is_zh_cn(letter):
            num += 1
    return num


def get_zh_code_num(word):
    num = 0
    for letter in word:
        if is_zh_code(letter):
            num += 1
    return num


def get_word_length(word):
    num = 0
    for letter in word:
        if is_zh_cn(letter) or is_zh_code(letter):
            num += 2
        else:
            num += 1
    return num
