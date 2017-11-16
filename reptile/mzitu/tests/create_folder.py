import os





# 编码转换 仅去除系统不允许的字符
def change_coding(in_str):
    # question_mark (question)(?)
    # 使用部分中文字符替换英文字符（操作系统限制）
    # 去除末尾可能存在的空格
    if __name__ == '__main__':
        in_str=in_str.replace('？', '(qm)')\
            .replace('?', '(qm)')\
            .replace(':', '：')

    out_str = ""
    # Win系统不允许的文件名 \ / : * ? " < > |
    remove_code = ["\\", "/", "*", "\"", "<", " > ", "|",]
    for item in in_str:
        if item in remove_code:
            out_str += ' '
        else:
            out_str += item

    out_str=out_str.strip()
    return out_str

file = open('name.txt', 'r', encoding='utf-8')
for line in file:
    print(change_coding(line))
