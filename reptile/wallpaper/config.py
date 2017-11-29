from urllib import parse

index_link = 'https://wall.alphacoders.com/?lang=Chinese'

# 浏览器标识
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

all_category = ['抽象', '动物', '动漫', '艺术', 'CGI', '卡通', '名人', '漫画', '黑暗', '自然', '奇幻', '食物', '游戏', '节日', '幽默', '人造', '人',
                '军事',
                '综合', '电影', '多屏', '音乐', '素材', '摄影', '产品', '宗教', '科幻', '运动', '电视剧', '技术', '座驾', '电子游戏', '武器', '女性']


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



'''测试'''
if __name__=='__main__':
    print(get_category_link(1))



