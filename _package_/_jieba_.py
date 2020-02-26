import jieba

data = ["全猪肉水饺", "巧克力蛋糕"]

for item in data:
    print(1, "/ ".join(jieba.cut(item, cut_all=True)))
    print(2, "/ ".join(jieba.cut(item, cut_all=False)))
    print(3, "/".join(jieba.cut_for_search(item)))
