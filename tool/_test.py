codes = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.'
# for code in codes:
#     print(code)
symbol='？'


pp='Ctrl + Space 基本的代码完成（类、方法、属性）'

# for item in pp:
#     if item in codes:
#         print('True---')
#     else:
#         print('False')
#

def is_zh_cn(letter):
    if '\u4e00' <= letter <= '\u9fff':
        return True
    else:
        return False

for p in pp:
    if is_zh_cn(p):
        print(p,end='   ')
        print('True--')
    else:
        print(p,end='   ')
        print('false')