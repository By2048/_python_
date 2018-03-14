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