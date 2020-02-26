from lxml import etree

data = """
<html><body>
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
</body></html>
"""

html = etree.HTML(data)
print(type(html))
result = etree.tostring(html, pretty_print=True)
print(result.decode())
print('-' * 88)

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
