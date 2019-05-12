
# 获取一个页面的最大图片数量 方便合成连接  40
# def get_max_image_num(link):
#     html = urllib.request.Request(link, headers=headers)
#     request = urllib.request.urlopen(html)
#     soup = BeautifulSoup(request, "html.parser")
#     for a in soup.find('div', class_='page').find_all('a'):
#         if (a.get_text() == '下一张'):
#             max_num = a.previous_sibling.previous_sibling.get_text()
#     return int(max_num)


# 获取已经下载的连接  has_down.txt -> has_down_list
# def get_has_down():
#     # file = open(has_down_path, 'r', encoding='utf-8')
#     with open(has_down_path, 'r', encoding='utf-8') as file:
#     # has_down = [line.strip() for line in file]
#         has_down = [line.split('|')[1].strip() for line in file]
#     return has_down


# 保存已经下载的链接到
# def keep_has_down(meizi):
#     has_down_txt = open('has_down.txt', 'a', encoding='utf-8')
#     has_down_txt.write(meizi.date + '\t' + '|' + '\t' +
#                        meizi.link + '\t' + '|' + '\t' + meizi.title + '\n')
#     has_down_txt.close()



