# # Coding=utf-8
# # Author By2048 Time 2017-1-18
# import os
# import urllib
# import urllib.request
# from bs4 import BeautifulSoup
# import multiprocessing
# import re
# import socket


start_url = 'http://www.mzitu.com/all'
# 获取主页下所有的meizi连接
def get_all_link(start_url):
    all_meizi_link = []
    html = urllib.request.Request(start_url, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    all_ul = soup.find_all('ul', class_='archives')
    for ul in all_ul:
        links = ul.find_all('a')
        for link in links:
            tmp = meizi(change_coding(link.get_text()), link['href'])
            all_meizi_link.append(tmp)
    return all_meizi_link



# 获取已经下载的图片链接
def get_has_down_by_txt():
    file = open(has_down_txt_path, 'r', encoding='utf-8')
    has_down = [line.split('<|>')[0].strip() for line in file]
    return has_down


# 保存已经下载的链接到
def keep_has_down_to_txt(meizi):
    has_down_txt = open(has_down_txt_path, 'a', encoding='utf-8')
    split_text = '\t' + '<|>' + '\t'
    has_down_txt.write(
        meizi.link + split_text +
        meizi.title + split_text +
        meizi.category + split_text +
        meizi.date + '\n')
    has_down_txt.close()

"""
CREATE TABLE has_down
(
  id         INTEGER PRIMARY KEY,
  link       TEXT     NOT NULL,
  title      TEXT     NOT NULL,
  category   TEXT     NOT NULL,
  date       TEXT     NOT NULL
);
select * from has_down
delete from has_down
SELECT link FROM has_down
"""

"""
CREATE TABLE error_down
(
  id         INTEGER PRIMARY KEY,
  link       TEXT     NOT NULL,
  title      TEXT     NOT NULL,
  category   TEXT     NOT NULL,
  date       TEXT     NOT NULL
);
"""



# 使用进程 获取主页连接下所有的图片下载连接
def get_down_link_list(link, max_num):
    pool_resule = []
    pool = multiprocessing.Pool(processes=pool_num)
    for cnt in range(1, max_num + 1):
        detail_link = link + '/' + str(cnt)
        pool_resule.append(pool.apply_async(get_img_down_link_list, (detail_link,)))
    pool.close()
    pool.join()
    # for tmp in pool_down_link:
    # 	print(tmp)
    # 	tmp_list.append(tmp.get())
    # down_link = [item for sub in tmp_list for item in sub]
    down_link = [item for sub in pool_resule for item in sub.get()]
    return down_link

# 编码转换 去除 非 汉字 英文字符
def change_coding_type_1(inStr):
    outStr = ""
    is_zh = re.compile(r"[\u4e00-\u9fff]")
    is_en = re.compile(r"[A-Za-z]")
    is_num = re.compile(r"[0-9]")
    is_spaces = re.compile(r"[\s]+")
    is_point = re.compile(r".")
    is_backslash = re.compile(r"\\")
    is_question_mark = re.compile(r"\?")
    is_exclamation_point = re.compile(r"! ")
    try:
        for word in inStr:
            if re.match(is_zh, word) != None:
                outStr += re.match(is_zh, word).group()
            elif re.match(is_en, word) != None:
                outStr += re.match(is_en, word).group()
            elif re.match(is_num, word) != None:
                outStr += re.match(is_num, word).group()
            elif re.match(is_spaces, word) != None:
                outStr += " "
            elif re.match(is_backslash, word) != None:
                outStr += ""
            elif re.match(is_point, word) != None:
                outStr += ""
            elif re.match(is_question_mark, word) != None:
                outStr += ""
            elif re.match(is_exclamation_point, word) != None:
                outStr += ""
    except:
        print("Change_Coding_Fail")
    finally:
        if (len(outStr) == 0):
            return "EmptyName"
        else:
            return outStr