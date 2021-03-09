from hanziconv import HanziConv

# 实现简繁体转换功能

print(HanziConv.toSimplified('繁簡轉換器'))
# 繁简转换器
print(HanziConv.toTraditional('繁简转换器'))
# 繁簡轉換器
print(HanziConv.toSimplified(u'繁簡轉換器'))
# 繁简转换器
print(HanziConv.toTraditional(u'繁简转换器'))
# 繁簡轉換器
print(HanziConv.toSimplified(u'mix English and Chinese. 繁簡轉換器'))
# mix English and Chinese. 繁简转换器
print(HanziConv.toTraditional(u'mix English and Chinese. 繁简转换器'))
# mix English and Chinese. 繁簡轉換器
print(HanziConv.toSimplified('mix English and Chinese. 繁簡轉換器'))
# mix English and Chinese. 繁简转换器
print(HanziConv.toTraditional('mix English and Chinese. 繁简转换器'))
# mix English and Chinese. 繁簡轉換器


print(u'繁簡轉換器' == u'繁简转换器')
# False
print(HanziConv.same(u'繁簡轉換器', u'繁简转换器'))
# True

str1 = 'mix English and Chinese. 繁簡轉換器'
str2 = 'mix English and Chinese. 繁简转换器'
str3 = 'mix Chinese and English. 繁简转换器'
str4 = u'mix English and Chinese. 繁簡轉換器'
print(HanziConv.same(str1, str2))
# True
print(HanziConv.same(str2, str3))
# False
print(HanziConv.same(str1, str4))
# True
