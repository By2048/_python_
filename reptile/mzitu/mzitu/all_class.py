# title
# link
# date
# category

# 连接名字 连接地址
class meizi_img:
    def __init__(self, title, link, category, date):
        self.title = title
        self.link = link
        self.category = category
        self.date = date

    def print_info(self):
        print('title'.ljust(10) + self.title)
        print('link'.ljust(10) + self.link)
        print()

    def print_all_info(self):
        print('title'.ljust(10) + self.title)
        print('link'.ljust(10) + self.link)
        print('category'.ljust(10) + self.category)
        print('date'.ljust(10) + self.date)
        print()


# 图片信息(Img)
class ImageInfo:
    FolderId = ""
    FolderName = ""
    Name = ""
    Path = ""
    Type = ""
    Size = ""  # 图片大小
    Width = ""
    Height = ""
    VisitDate = ""  # 文件最后访问时间
    CreateDate = ""  # 文件创建时间
    ChangeDate = ""  # 文件最后修改时间

    def __init__(self, folderId, folderName, name, path, type, size, width, heigth, visitDate, createDate, changeDate):
        self.FolderId = folderId
        self.FolderName = folderName
        self.Name = name
        self.Path = path
        self.Type = type
        self.Size = size
        self.Width = width
        self.Height = heigth
        self.VisitDate = visitDate
        self.CreateDate = createDate
        self.ChangeDate = changeDate

    def print_info(self):
        print('FolderId'.ljust(10) + self.FolderId)
        print('Name'.ljust(10) + self.Name)
        print('Path'.ljust(10) + self.Path)
        print('Type'.ljust(10) + self.Type)
        print('Size'.ljust(10) + self.Size)
        print('Width'.ljust(10) + self.Width)
        print('Height'.ljust(10) + self.Height)
        print('VisitDate'.ljust(10) + self.VisitDate)
        print('CreateDate'.ljust(10) + self.CreateDate)
        print('ChangeDate'.ljust(10) + self.ChangeDate)
        print()


# 文件夹信息
class FolderInfo:
    Name = ""
    Path = ""
    CreateDate = ""  # 文件夹创建时间
    ImgNum = ""
    TotalSize = ""

    def __init__(self, name, path, createDate, imgNum, totalSize):
        self.Name = name
        self.Path = path
        self.CreateDate = createDate
        self.ImgNum = imgNum
        self.TotalSize = totalSize

    def print_info(self):
        print('Name'.ljust(10) + self.Name)
        print('Path'.ljust(10) + self.Path)
        print('CreateDate'.ljust(10) + self.CreateDate)
        print('ImgNum'.ljust(10) + self.ImgNum)
        print('TotalSize'.ljust(10) + self.TotalSize)
        print()
