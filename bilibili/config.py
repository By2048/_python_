import pymysql

image_keep_path = "F:\\- BiliBili"

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

db=pymysql.connect('localhost','root','admin','bilibili')

step=5

# 全部 最热
all_hot='http://h.bilibili.com/eden/draw_area#/all/hot‘'
# 全部 最新
all_new='http://h.bilibili.com/eden/draw_area#/all/new'


# 插画 最热
illustration_hot='http://h.bilibili.com/eden/draw_area#/illustration/hot'
# 插画 最新
illustration_new='http://h.bilibili.com/eden/draw_area#/illustration/new'

# 漫画 最热
comic_hot='http://h.bilibili.com/eden/draw_area#/comic/hot'
# 漫画 最新
comic_new='http://h.bilibili.com/eden/draw_area#/comic/hot'

# 其他 最热
other_hot='http://h.bilibili.com/eden/draw_area#/other/hot'
# 其他 最新
other_new='http://h.bilibili.com/eden/draw_area#/other/new'

# 摄影 cos
pic_cos='http://h.bilibili.com/eden/picture_area#/?class=cos'

# 绘画 全部
draw_all='http://h.bilibili.com/eden/picture_area#/?class=draw'


# 排行榜 画友 首页
draw_rank_index='http://h.bilibili.com/common/rank#/draw'
# 画友 周榜
draw_week='http://h.bilibili.com/common/ranklist?biz=draw&type=week'
# 画友 月榜
draw_month='http://h.bilibili.com/common/ranklist?biz=draw&type=month'
# 画友 新人榜
draw_new_person='http://h.bilibili.com/common/ranklist?biz=draw&type=day'


# 摄影 首页
photo_index='http://h.bilibili.com/common/rank#/photo'
# 摄影 cos 周榜
cos_week='http://h.bilibili.com/common/ranklist?biz=photo&category=cos&type=week'
# 摄影 cos 月榜
cos_month='http://h.bilibili.com/common/ranklist?biz=photo&category=cos&type=month'
# 摄影 cos 新人榜
cos_day='http://h.bilibili.com/common/ranklist?biz=photo&category=cos&type=day'
















