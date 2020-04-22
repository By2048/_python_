import os
import re
import subprocess

adb_path = r'D:\Android\Adb\adb.exe'
adb_connect = '3.1.1.3:5555'
aapt_path = r'D:\Android\aapt.exe'
backup_path = r'T:\phone'
phone_folder = '/storage/emulated/0/'


def init():
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)


def connect_adb():
    os.system(f'{adb_path} connect {adb_connect}')


def disconnect_adb():
    os.system(f'{adb_path} disconnect {adb_connect}')


def get_all_app_package():
    command = f'{adb_path} shell pm list packages -3'
    data = os.popen(command)
    app_packages = [item.replace('package:', '').rstrip() for item in data]
    return app_packages


def get_app_path(app_package):
    command = f'{adb_path} shell pm path {app_package}'
    path = os.popen(command).read().replace('package:', '').strip()
    return path


def backup_app(app_path):
    command = f"{adb_path} pull {app_path} {os.path.join(backup_path, 'base.apk')}"
    os.system(command)


def get_app_info(apk_path):
    data = subprocess.run(f'{aapt_path} dump badging {apk_path}',
                          stdout=subprocess.PIPE,
                          encoding='utf8')
    data = data.stdout

    package = re.compile(r"(?<=package: name=')(.*?)(?=')").findall(data)
    app_name = re.compile(r"(?<=application-label:')(.*?)(?=')").findall(data)
    app_name_zh_cn = re.compile(r"(?<=application-label-zh-CN:')(.*?)(?=')").findall(data)
    version_name = re.compile(r"(?<=versionName=')(.*?)(?=')").findall(data)

    app_name = app_name_zh_cn if app_name_zh_cn else app_name
    if not app_name:
        app_name = package

    package, app_name, version_name = package[0], app_name[0], version_name[0]

    return app_name, version_name


def rename_base_apk():
    old_name = os.path.join(backup_path, 'base.apk')

    if not os.path.exists(old_name):
        return

    app_name, version_name = get_app_info(old_name)

    _name_ = f"{app_name} - {version_name}.apk"
    _name_ = _name_.replace('\\', '').replace('/', '')
    new_name = os.path.join(backup_path, _name_)

    os.rename(old_name, new_name)


def test():
    pass


def main():
    init()
    # connect_adb()
    app_packages = get_all_app_package()
    for app_package in app_packages:
        app_path = get_app_path(app_package)
        backup_app(app_path)
        rename_base_apk()
    print()
    # disconnect_adb()


if __name__ == '__main__':
    main()
