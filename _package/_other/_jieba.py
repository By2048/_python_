# encoding=utf-8
import jieba

datas = ["全猪肉水饺", "巧克力蛋糕"]

jieba.load_userdict("userdict.txt")

for data in datas:
    print("Full Mode: " + "/ ".join(jieba.cut(data, cut_all=True)))
    print("Default Mode: " + "/ ".join(jieba.cut(data, cut_all=False)))
    print("/".join(jieba.cut_for_search(data)))
    print()
