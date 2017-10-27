import sys
from bilibili.main import *

# sys.path.append('..')

try:
    from .tool import *
except ImportError:
    from tool import *

str_list=[str(i) for i in range(8)]

lll='''insert into image(name,down_link,author,detail_link,num,create_date,category,tag,character_name,source,discription)'''
print(lll)

ppp='''values (''067b.jpg<->0b.jpg'', ''http://i0.hlb.com/bfs/vc/06acab.jpg<->http://i0.hdslb.com/bfs/vc/06b.jpg'', ''Endsmall敏'', ''http://h.bilibili.com/782375'', '2', ''2017-10-25 16:01:22'', ''画友<->插画'', ''萝莉<->体操服'', ''角色：<->五岛润'',''来源：<->天使的3p！，<->萝莉，<->pixiv，<->幼女'',''之前画的。不用多说。萝莉赛高！（p站有污）'');'''

print(ppp)