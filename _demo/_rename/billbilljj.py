import os

replaces_data = [
    ('【', '['),
    ('】', ']'),
    ('BilibiliJJ.COM-[MMD]', ''),
    ('_', ''),
    ('[MMD]', '')
]

download_path = r'f:\video\MMD\MMD'
for name in os.listdir(download_path):
    old_name = os.path.join(download_path, name)
    new_name = old_name
    for item in replaces_data:
        new_name = new_name.replace(item[0], item[1])
    new_name = new_name.strip()
    print(f'old_name   {old_name}\nnew_name   {new_name}\n')
    os.rename(old_name, new_name)
