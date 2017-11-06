import re
import os

def run_cmd(cmd):
    lines=[]
    for line in os.popen(cmd).readlines():
        lines.append(line.replace('''\n''',''))
    line_str = "".join(lines)
    return line_str

if __name__=='__main__':
    line_str=run_cmd('ipconfig')
    singleNet_span=re.search(r'singleNetPPPoE:',line_str).span()[1]
    singleNet_info=line_str[singleNet_span:]

    re_ip_rule=(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    ip_address=re.search(re_ip_rule,singleNet_info).group()

    print('\n\n')
    print(ip_address)
    print('\n')
