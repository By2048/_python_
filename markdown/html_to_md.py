from bs4 import *



def get_main_body(soup):
    lines=[]
    first_th=[item.get_text() for item in soup.find('tr').find_all('th')]
    if len(first_th)!=0:
        lines.append("\t".join(first_th))
    for tr in soup.find_all('tr')[1:]:
        all_td=[]
        for td in tr.find_all('td'):
            if len(tr.find_all('td')) != 0:
                if td.find('ul') != None:
                    all_li= [item.get_text() for item in td.find('ul').find_all('li')]
                    all_td.append(" ".join(all_li))
                else:
                    all_td.append(td.get_text())
        lines.append("\t".join(all_td))
    return lines

if __name__ == '__main__':

    print('\n输入以 ==== 结束\n')

    str_in = []

    sentinel = '===='  # 遇到这个就结束
    for line in iter(input, sentinel):
        str_in.append(line)

    soup = BeautifulSoup("".join(str_in), "lxml")

    lines=get_main_body(soup)

    for line in lines:
        print(line)
