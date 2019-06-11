from lxml import etree

html = etree.parse('hello.html')
result = etree.tostring(html, pretty_print=True)
print(result)

print('-' * 88)
# 获取所有的 <li> 标签ox
print(type(html))
result = html.xpath('//li')
print(result)
print(len(result))
print(type(result))
print(type(result[0]))

print('-' * 88)
# 获取 <li> 标签的所有 class
result = html.xpath('//li/@class')
print(result)

print('-' * 88)
result = html.xpath('//li/a[@href="link1.html"]')
print(result)

