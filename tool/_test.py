# lengths=[[get_word_length(item) for item in line.split('\t')] for line in input_lines]

def get_splite_items(line):
    item_tab=line.split('\t')
    item_space=line.split('    ')
    if len(item_tab)>len(item_space):
        items=item_tab
    elif len(item_tab)<len(item_space):
        items=item_space
    else:
        items=item_tab
    return items


pp1='Ctrl + Space    基本的代码完成（类、方法、属性）'
pp2='Ctrl + Space	基本的代码完成（类、方法、属性）'



print(get_splite_items(pp1))
print(get_splite_items(pp2))