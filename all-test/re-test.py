# -*- coding: utf-8 -*- 
import sys
import re

s="""
            en: Regular expression is a powerful tool for manipulating text. 
            zh: 汉语是世界上最优美的语言，正则表达式是一个很有用的工具
            jp: 正規表現は非常に役に立つツールテキストを操作することです。 
            jp-char: あアいイうウえエおオ 
            kr:정규 표현식은 매우 유용한 도구 텍스트를 조작하는 것입니다. 
            """

print("原始utf8字符")
print("--------")
print(repr(s))
print("--------\n")

#非ansi
re_words=re.compile(r"[\x80-\xff]+")
m =  re_words.search(s,0)
print("非ansi字符")
print("--------")
print(m)
print(m.group())
print("--------\n")

# #unicode
# s = unicode(s)
# print("原始unicode字符")
# print("--------")
# print(repr(s))
# print("--------\n")
#
# #unicode chinese
# re_words = re.compile(u"[\u4e00-\u9fa5]+")
# m =  re_words.search(s,0)
# print("unicode 中文")
# print("--------")
# print(m)
# print(m.group())
# res = re.findall(re_words, s)       # 查询出所有的匹配字符串
# if res:
#     print("There are %d parts:\n"% len(res)
#     for r in res:
#         print("\t",r )
#         print()
# print("--------\n")
#
#
# #unicode korean
# re_words=re.compile(u"[\uac00-\ud7ff]+")
# m =  re_words.search(s,0)
# print("unicode 韩文")
# print("--------")
# print(m)
# print(m.group())
# print("--------\n")
#
#
# #unicode japanese katakana
# re_words=re.compile(u"[\u30a0-\u30ff]+")
# m =  re_words.search(s,0)
# print("unicode 日文 片假名")
# print("--------")
# print(m)
# print(m.group())
# print("--------\n")
#
#
# #unicode japanese hiragana
# re_words=re.compile(u"[\u3040-\u309f]+")
# m =  re_words.search(s,0)
# print("unicode 日文 平假名")
# print("--------")
# print(m)
# print(m.group())
# print("--------\n")
#
#
# #unicode cjk Punctuation
# re_words=re.compile(u"[\u3000-\u303f\ufb00-\ufffd]+")
# m =  re_words.search(s,0)
# print("unicode 标点符号")
# print("--------")
# print(m)
# print(m.group())
# print("--------\n")
