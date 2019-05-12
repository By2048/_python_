# coding=utf-8
def get_zh_num(codes):
    def zh_cn(letter):
        return '\u4e00' <= letter <= '\u9fff'

    def zh_code(symbol):
        codes = ("└＾＜｜〛＼〾〝〃＇＋〜＃〚〿“「、‘＄）"
                 "【＆】；％＝’…｛｀｠〘﹏｟。＠〔［，－╚／？＞｝"
                 "〟〰《–—」〙〕］（”〈〉』！·〞『：＂＿〗┐～╗〖》＊↓↑←→")
        return symbol in codes

    zh_num = 0
    for item in codes:
        if zh_cn(item) or zh_code(item):
            zh_num += 1
    return zh_num


if __name__ == '__main__':
    pass
