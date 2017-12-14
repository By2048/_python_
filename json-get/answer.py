import re


def addword(dic, b='', fword=['0']):
    fword.pop()
    for i in dic:
        print(i)
        a = b + i + '.'
        fword.append(a)

    if isinstance(dic[i], list):
        fword.pop()
        for j in dic[i]:
            c = a
            a = a + j
            fword.append(a)
            a = c
            a = ''

    if isinstance(dic[i], dict):
        addword(dic[i], b=fword[-1], fword=fword)
        return fword


def searchdic(dic, searchword):
    fword = addword(dic, b='', fword=['0'])
    reword = re.compile(r'(.*?{})'.format(searchword))
    for i in fword:
        searchout = re.findall(reword, i)
        if searchout == []:
            print('不存在的关键字：' + searchword)
        else:
            print(searchout[0])


tdic = {"奴隶社会": {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]},
                 "欧洲": {"希腊罗马古典文化": ["建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"], "希腊": ["希腊城邦", "雅典民主"]},
                 "非洲": {"古埃及文明": ["金字塔"]}}}

searchdic(tdic, "金字塔")

searchdic(tdic, "美洲")
