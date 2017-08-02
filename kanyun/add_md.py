import os


def create_md(rootPath):
    for root, dirs, files in os.walk(rootPath):
        for dir in dirs:
            print(dir)
            if dir=='images':
                continue

            _files=os.listdir(os.path.join(root,dir))
            print(_files)

            if (dir+'.md') in _files:
                print('exit .md')
            else:
                _path=os.path.join(root,dir)+'\\'+dir+'.md'
                print('create .md    '+_path)
                with open(_path,'w') as file:
                    file.close()
            print('\n')

if __name__ == '__main__':
    rootPath = r'F:\- Test\c-sharp'
    create_md(rootPath)


