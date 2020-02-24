import requests


class Progress(object):
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0, unit='', sep='/',
                 chunk_size=1.0):
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.statue)
        self.unit = unit
        self.seq = sep

    def __str__(self):
        # 【名称】状态 进度 单位 分割线 总数 单位

        return "[%s] %s %.2f %s %s %.2f %s".format(
            self.title, self.status,
            self.count / self.chunk_size,
            self.unit, self.seq,
            self.total / self.chunk_size,
            self.unit
        )

    def refresh(self, count=1, status=None):
        self.count += count
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status

        print(self, end=end_str)


def main():
    from contextlib import closing

    url = "https://download.microsoft.com/download/8/7/D/87D36A01-1266-4FD3-924C-1F1F958E2233/Office2010DevRefs.exe"

    with closing(requests.get(url, stream=True)) as response:
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        """
        需要根据 response.status_code 的不同添加不同的异常处理
        """
        print('content_size', content_size, response.status_code, )
        progress = Progress("razorback", total=content_size, unit="KB", chunk_size=chunk_size,
                            run_status="正在下载", fin_status="下载完成")
        # chunk_size = chunk_size < content_size and chunk_size or content_size
        with open('./file.zip', "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.refresh(count=len(data))

        print('下载完成', )


def test():
    # url = "https://download.microsoft.com/download/8/7/D/87D36A01-1266-4FD3-924C-1F1F958E2233/Office2010DevRefs.exe"
    url = "http://pic37.nipic.com/20140113/8800276_184927469000_2.png"
    data = requests.get(url)
    print(data)


if __name__ == '__main__':
    test()
