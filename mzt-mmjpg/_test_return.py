def F1(x, y):
    a = x - y
    b = x + y
    return a, b # 也可以写作 return a, b

(c, d) = F1(9, 4)  # 也可以写作 c , d = F1 ( 9, 4 )

print(c, d)


# 获取一个页面的最大图片数量 方便合成连接  40
# def get_max_image_num(link):
#     html = urllib.request.Request(link, headers=headers)
#     request = urllib.request.urlopen(html)
#     soup = BeautifulSoup(request, "html.parser")
#     for a in soup.find('div', class_='page').find_all('a'):
#         if (a.get_text() == '下一张'):
#             max_num = a.previous_sibling.previous_sibling.get_text()
#     return int(max_num)
#
#
# def get_first_img_down_link(link):
#     html = urllib.request.Request(link, headers=headers)
#     request = urllib.request.urlopen(html)
#     soup = BeautifulSoup(request, "html.parser")
#     imgs = soup.find('div', class_='content').find('img')
#     return imgs['src']
