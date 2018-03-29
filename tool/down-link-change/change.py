import base64
import urllib.parse
import sys
import re

# 迅雷下载地址编码方式
# 在原地址前面加"AA"，后面加"ZZ"，地址变为 AA（original_link）ZZ
# 添加 AA,ZZ 后地址使用base64编码
# 地址前加 thunder://
def thunder_to_original(link):
    return base64.b64decode(link[10:]).decode('utf-8')[2:-2]
def original_to_thunder(link):
    add_link=str("AA"+link+"ZZ") # str
    temp=bytes(add_link,encoding='utf-8') # bytes
    outlink=base64.b64encode(temp) # bytes
    return "thunder://"+str(outlink,encoding='utf-8') # str

# QQ旋风下载地址编码方式
# 将原地址直接base64编码
# 地址前加 qqdl://
def qqdl_to_original(link):
    return base64.b64decode(link[7:]).decode('utf-8')
def original_to_qqdl(link):
    temp=bytes(link,encoding='utf-8') # bytes
    outlink=base64.b64encode(temp) # bytes
    return "qqdl://"+str(outlink,encoding='utf-8') # str

# 快车下载地址编码方式
# 在原地址前后都加上"[FLASHGET]"，地址变为 [FLASHGET]（original_link）[FLASHGET]
# 地址使用base64编码
# 地址前加flashget://
# 注意后面还要加上"&符号"，最后面加的是个人信息
# example Flashget://W0ZMQVNEdFVF0=&yinbing1986
def flashget_to_original(link):
    return base64.b64decode(link[11:]).decode('utf-8')[10:-10]
def original_to_flashget(link):
    add_link=str("[FLASHGET]"+link+"[FLASHGET]") # str
    temp=bytes(add_link,encoding='utf-8') # bytes
    outlink=base64.b64encode(temp) # bytes
    return "flashget://"+str(outlink,encoding='utf-8') # + "&AM" # str

# 解析 utf-8 的 url 地址
def original_to_text(link):
    return urllib.parse.unquote(link)
def text_to_original(link):
    return urllib.parse.quote(link)

def print_links(links):
    print("{:<11s}".format("flashget:"),end="")
    print(links[0])
    print("{:<11s}".format("qqdl"),end="")
    print(links[1])
    print("{:<11s}".format("thunder"),end="")
    print(links[2])
    print("{:<11s}".format("original"),end="")
    print(links[3])

def thunder_to_other(thunder_link):
    original_link=thunder_to_original(thunder_link)
    qqdl_link=original_to_qqdl(original_link)
    flashget_link=original_to_flashget(original_link)
    links=[flashget_link,qqdl_link,thunder_link,original_link]
    return links
def flashget_to_other(flashget_link):
    original_link=flashget_to_original(flashget_link)
    qqdl_link=original_to_qqdl(original_link)
    thunder_link=original_to_thunder(original_link)
    links=[flashget_link,qqdl_link,thunder_link,original_link]
    return links
def qqdl_to_other(qqdl_link):
    original_link=qqdl_to_original(qqdl_link)
    thunder_link=original_to_thunder(original_link)
    flashget_link=original_to_flashget(original_link)
    links=[flashget_link,qqdl_link,thunder_link,original_link]
    return links
def original_to_other(original_link):
    thunder_link=original_to_thunder(original_link)
    qqdl_link=original_to_qqdl(original_link)
    flashget_link=original_to_flashget(original_link)
    links=[flashget_link,qqdl_link,thunder_link,original_link]
    return links

if __name__=="__main__":
    print("Start")
    link=sys.stdin.readline()
    if re.search('flashget://',link,re.IGNORECASE)!=None: # 快车下载连接
        print("is_flashget")
        links = flashget_to_other(link)
    elif re.search('qqdl://',link,re.IGNORECASE)!=None:  # QQ旋风下载连接
        print("is_qqdl")
        links = qqdl_to_other(link)
    elif re.search('thunder://',link,re.IGNORECASE)!=None: # 迅雷下载连接
        print("is_thunder")
        links=thunder_to_other(link)
    else:   # 原始下载连接
        print("is_original")
        links=original_to_other(link)
    print_links(links)

    original_link="http://sw.bos.baidu.com/sw-search-sp/software/84765693d3add/pcmaster_6.2.1.0_full.zip"
    thunder_link = original_to_thunder(original_link)
    qqdl_link = original_to_qqdl(original_link)
    flashget_link = original_to_flashget(original_link)
    links = [flashget_link, qqdl_link, thunder_link, original_link]
    for link in links:
        print(link)
