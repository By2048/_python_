class bili_img:
    # name,author,down_link,detail_link,num,upload_time,tag,md5,character_name,source_anime,discription

    # name
    # author
    # down_link
    # detail_link
    # num
    # upload_time
    # tag
    # character_name
    # source_anime
    # discription

    def __init__(self,name,author,detail_link,down_link,num,upload_time,
                 tag,md5,character_name,source_anime,discription):
        self.name=name
        self.author=author
        self.detail_link=detail_link
        self.down_link=down_link
        self.num=num
        self.upload_time=upload_time
        self.tag=tag
        self.character_name=character_name
        self.source_anime=source_anime
        self.discription=discription

    def print_first(self):
        print('name'.ljust(20,' ')+self.name[0])
        print('author'.ljust(20,' ')+str(self.author))
        print('detail_detail'.ljust(20,' ')+self.detail_link)
        print('down_link'.ljust(20,' ')+self.down_link[0])
        print()

    def print_all(self):
        print('name'.ljust(20,' ')+" ".join(self.name))
        print('author'.ljust(20,' ')+str(self.author))
        print('detail_detail'.ljust(20,' ')+self.detail_link)
        print('down_link'.ljust(20,' ')+" ".join(self.down_link))
        print('num'.ljust(20,' ')+str(self.num))
        print('upload_time'.ljust(20,' ')+str(self.upload_time))
        print('tag'.ljust(20,' ')+str(self.tag))
        print('md5'.ljust(20,' ')+str(self.md5))
        print('character_name'.ljust(20,' ')+str(self.character_name))
        print('source_anime'.ljust(20,' ')+str(self.source_anime))
        print('discription'.ljust(20,' ')+str(self.discription))
        print()
