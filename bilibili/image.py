class bili_img:
    # id,name,author,down_link,num,upload_time,tag,md5,character_name,source_anime,discription

    # id
    # name
    # author
    # down_link
    # num
    # upload_time
    # tag
    # md5
    # character_name
    # source_anime
    # discription

    def __init__(self,id,name,author,down_link,num,upload_time,
                 tag,md5,character_name,source_anime,discription):
        self.id=id
        self.name=name
        self.author=author
        self.down_link=down_link
        self.num=num
        self.upload_time=upload_time
        self.tag=tag
        self.md5=md5
        self.character_name=character_name
        self.source_anime=source_anime
        self.discription=discription

    def print(self):
        print('id'.ljust(20,' ')+str(self.id))
        print('name'.ljust(20,' ')+str(self.name))
        print('author'.ljust(20,' ')+str(self.author))
        print('down_link'.ljust(20,' ')+str(self.down_link))
        print('num'.ljust(20,' ')+str(self.num))
        print('upload_time'.ljust(20,' ')+str(self.upload_time))
        print('tag'.ljust(20,' ')+str(self.tag))
        print('md5'.ljust(20,' ')+str(self.md5))
        print('character_name'.ljust(20,' ')+str(self.character_name))
        print('source_anime'.ljust(20,' ')+str(self.source_anime))
        print('discription'.ljust(20,' ')+str(self.discription))

