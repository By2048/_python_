import os

download_path = '/home/download/wallpaper'

file_list_path = '/home/download/wallpaper/file_list.txt'

# download_path = 'T:\\_tmp'
# file_list_path = 'T:\\_tmp\\file_list.txt'
#

def get_down_link():
    down_links = []
    with open(file_list_path, 'r') as file:
        for line in file.readlines():
            down_links.append(line.replace('\n', ''))
    return down_links


def is_down(file_name):
    has_downs = os.listdir(download_path)
    if file_name in has_downs:
        return True
    else:
        return False


def start_down():
    downl_links = get_down_link()
    for link in downl_links:
        image_name = os.path.basename(link)
        if is_down(image_name) == False:
            os.system('wget {0}'.format(link))
        else:
            pass

start_down()