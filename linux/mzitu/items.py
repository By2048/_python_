# title
# link
# date
# category

# 连接名字 连接地址
class Meizi:
    def __init__(self, id, title, link, category, date):
        self.id = id
        self.title = title
        self.link = link
        self.category = category
        self.date = date

    def print_simple_info(self):
        print('title'.ljust(10) + self.title)
        print('link'.ljust(10) + self.link)
        print()

    def print_all_info(self):
        print('id'.ljust(10) + self.id)
        print('title'.ljust(10) + self.title)
        print('link'.ljust(10) + self.link)
        print('category'.ljust(10) + self.category)
        print('date'.ljust(10) + self.date)
        print()


# 图片信息(Img)
class MImage:
    def __init__(self, folderid, foldername, name, path, type, size, width, heigth,
                 visitdate, createdate, changedate):
        self.folderid = folderid
        self.foldername = foldername
        self.name = name
        self.path = path
        self.type = type
        self.size = size
        self.width = width
        self.height = heigth
        self.visitdate = visitdate
        self.createdate = createdate
        self.changedate = changedate

    def print_info(self):
        print('folderid'.ljust(10) + self.folderid)
        print('name'.ljust(10) + self.name)
        print('path'.ljust(10) + self.path)
        print('type'.ljust(10) + self.type)
        print('size'.ljust(10) + self.size)
        print('width'.ljust(10) + self.width)
        print('height'.ljust(10) + self.height)
        print('visitdate'.ljust(10) + self.visitdate)
        print('createdate'.ljust(10) + self.createdate)
        print('changedate'.ljust(10) + self.changedate)
        print()


# 文件夹信息
class MFolder:
    def __init__(self, name, path, createdate, imgnum, totalsize):
        self.name = name
        self.path = path
        self.createdate = createdate
        self.imgnum = imgnum
        self.totalsize = totalsize

    def print_info(self):
        print('name'.ljust(10) + self.name)
        print('path'.ljust(10) + self.path)
        print('createdate'.ljust(10) + self.createdate)
        print('imgnum'.ljust(10) + self.imgnum)
        print('totalsize'.ljust(10) + self.totalsize)
        print()
