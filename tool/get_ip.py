import re
import os
import sys

sys.path.append("..")

try:
    from qqmail.mail_txt import *
except ImportError:
    from ..qqmail.mail_txt import *


def run_cmd(cmd):
    lines = []
    for line in os.popen(cmd).readlines():
        lines.append(line.replace('''\n''', ''))
    line_str = "".join(lines)
    return line_str


if __name__ == '__main__':
    line_str = run_cmd('ipconfig')
    singleNet_span = re.search(r'singleNetPPPoE:', line_str).span()[1]
    singleNet_info = line_str[singleNet_span:]

    re_ip_rule = (r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    ip_address = re.search(re_ip_rule, singleNet_info).group()

    print('\n\n')
    print(ip_address)
    print('\n')

    mail_txt(ip_address,to_address='1247079575@qq.com',from_title='am-pc ip',to_title='am-phone',topic=ip_address)
    print('\n')
