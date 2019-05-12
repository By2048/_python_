import os
import sys
import subprocess
import command

# def run_cmd(cmd):
#     lines=[]
#     # for line in os.popen(cmd).readlines():
#     #     lines.append(line.replace('''\n''',''))
#     with open(file_path, encoding='utf-8') as data_file:
#         data_file.write(os.popen(cmd))
#     # for line in lines:
#     #     print(repr(line))


import subprocess

p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line, )
retval = p.wait()
print(retval)

if __name__ == '__main__':
    cmd_sr = 'node E:\\Desktop\\MarkDownToHtml\\make.js'
    # out_put=os.system(cmd_sr)

    # output = os.popen('cat /proc/cpuinfo')
    # print(output.read())

    # print(out_put.read())
    file_path = "f:\\keep.txt"
    # with open(file_path,'w') as file:
    #     file.write(os.system(cmd_sr))

    # tmps = os.popen(cmd_sr).readlines()
    # for tmp in tmps:
    #     print(tmp, end='')
    # utf8  gbk encode  decode
    # run_cmd('chcp 65001')
    # run_cmd(cmd_sr)

    # p = os.popen("node E:\\Desktop\\MarkDownToHtml\\make.js", 'r')
    # print(p.read())

    pp = subprocess.check_output(cmd_sr)
    with open(file_path, 'wb') as file:
        file.write(pp)
