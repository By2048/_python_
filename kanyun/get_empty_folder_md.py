import os


def is_Yu_Writer_folder(path):
    split_paths = path.split('.')
    if len(split_paths)==1:
        return False
    if split_paths[1] =='resource':
        return True
    else:
        return False

def is_git_folder(path):
    split_paths=path.split('\\')
    is_git=False
    for path in split_paths:
        if path =='.git':
            return True
    return is_git

def create_md(rootPath):
    for root, dirs, files in os.walk(rootPath):
        for dir in dirs:

            if dir[0] in ['_','.']:
                continue

            file_path=os.path.join(root,dir)
            if is_git_folder(file_path)==True:
                continue
            # print(is_Yu_Writer_folder(file_path))
            if is_Yu_Writer_folder(file_path) == True:
                continue


            _files=os.listdir(os.path.join(root,dir))
            # print(_files)

            if (dir+'.md') in _files: # exit .md
                pass
                # print('exit .md')
            else:
                _path=os.path.join(root,dir)+'\\'+dir+'.md'
                print('create [folder].md    '+_path)
                with open(_path,'w') as file:
                    file.close()


if __name__ == '__main__':
    # Test...
    rootPath = r'E:\Desktop\NoteBook\Python'
    create_md(rootPath)

    # print(is_git_folder('F:\\- Test\\Python\\.git'))


