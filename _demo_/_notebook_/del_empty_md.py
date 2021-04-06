import os

def remove_empty_md(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.md') and os.path.getsize(os.path.join(root,file))==0:
                path=os.path.join(root,file)
                print(path.ljust(30)+str(os.path.getsize(os.path.join(root,file))))
                os.remove(path)


if __name__=='__main__':
    rootPath = r'E:\Desktop\NoteBook'
    remove_empty_md(rootPath)