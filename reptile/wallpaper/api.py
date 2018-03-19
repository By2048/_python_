api_code='cbf61fb8197d5fdc054041c1bd2945e9'

'''150,000个查询/月'''


'''

newest
此方法返回按最新排序的壁纸。

highest_rated
此方法返回按照评分排序的壁纸。



//调用api页面
$ test = file_get_contents（“https://wall.alphacoders.com/api2.0/get.php?auth=YOUR_KEY&method=wallpaper_count”）;
//解码json输出
$ results = json_decode（$ test，true）;

//一切都很顺利
如果（$ results ['success']）
{
    //显示计数
    回声“壁纸计数：”。$结果[ '计数'];
}



'''


"""
1 Abstract 12121
2 Animal 48618
3 Anime 136054
4 Artistic 16950
6 Cartoon 3560
7 Celebrity 25187
5 CGI 3073
8 Comics 24324
9 Dark 6461
10 Earth 57800
11 Fantasy 21012
12 Food 13473
14 Game 1391
15 Holiday 6532
13 Humor 2616
16 Man Made 31369
17 Men 457
18 Military 9661
19 Misc 3736
20 Movie 41641
21 Multi Monitor 1782
22 Music 24072
23 Pattern 1930
24 Photography 17180
25 Products 989
26 Religious 2893
27 Sci Fi 15256
28 Sports 7433
30 Technology 3953
29 TV Show 18150
31 Vehicles 55736
32 Video Game 72821
34 Weapons 1949
33 Women 31603
"""

from urllib import parse

api_code='cbf61fb8197d5fdc054041c1bd2945e9'

index_link = 'https://wall.alphacoders.com/?lang=Chinese'


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

all_category = ['抽象', '动物', '动漫', '艺术', 'CGI', '卡通', '名人', '漫画',
                '黑暗', '自然', '奇幻', '食物', '游戏', '节日', '幽默', '人造',
                '人','军事','综合', '电影', '多屏', '音乐', '素材', '摄影', '产品',
                '宗教', '科幻', '运动', '电视剧', '技术', '座驾', '电子游戏', '武器', '女性']


'''
根据 id page 获取分类链接
args:
    id 分类的id
    page 第几页，默认第一页，可省略
returns:
    link 分类的链接地址
'''
def get_category_link(id,page=1):
    name = parse.quote(all_category[id - 1])
    link = 'https://wall.alphacoders.com/by_category.php?id=' + str(id) + '&name=' + name + '&lang=Chinese'+'&page='+str(page)
    return link



if __name__=='__main__':
    print(get_category_link(1))
