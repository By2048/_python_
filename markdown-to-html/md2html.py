#md2html.py
import markdown

path_1=r'E:\Desktop\input.md'

path_2=r'E:\Desktop\output.html'

with open(path_1,'r',encoding='utf8') as f:
    for line in f.readlines():
        html=markdown.markdown(line)
        print(html)