import sys

if sys.platform == 'linux':
    download_path = '/root/share/mzitu'
elif sys.platform == 'win32':
    download_path = 'R:\\Image\\mzitu'
else:
    download_path = ''
    raise Exception('获取下载路径出错')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, likez Gecko)'
                         'Chrome/53.0.2785.143 Safari/537.36'}

images_link = 'http://www.mzitu.com/all'

images_link_old = 'http://www.mzitu.com/old'

start_link = 'http://www.mzitu.com'


def test():
    print(f"keep_path    {download_path}")
    print(f"headers      {headers}")
    print(f"images_link  {images_link}")
    print(f"start_link   {start_link}")


if __name__ == '__main__':
    test()
