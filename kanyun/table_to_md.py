from bs4 import *

html_str='''
<table class="dataintable">

<tbody><tr>
<th style="width:20%;">属性</th>
<th>值</th>
<th>描述</th>
</tr>

<tr>
<td><a href="/tags/att_link_charset.asp" title="HTML <link> 标签的 charset 属性">charset</a></td>
<td><i>char_encoding</i></td>
<td><span class="deprecated">HTML5 中不支持。</span></td>
</tr>

<tr>
<td><a href="/tags/att_link_href.asp" title="HTML5 <link> href 属性">href</a></td>
<td><i>URL</i></td>
<td>规定被链接文档的位置。</td>
</tr>

<tr>
<td><a href="/tags/att_link_hreflang.asp" title="HTML5 <link> hreflang 属性">hreflang</a></td>
<td><i>language_code</i></td>
<td>规定被链接文档中文本的语言。</td>
</tr>

<tr>
<td><a href="/tags/att_link_media.asp" title="HTML5 <link> media 属性">media</a></td>
<td><i>media_query</i></td>
<td>规定被链接文档将被显示在什么设备上。</td>
</tr>

<tr>
<td><a href="/tags/att_link_rel.asp" title="HTML5 <link> rel 属性">rel</a></td>
<td>
	<ul>
        <li>alternate</li>
        <li>author</li>
        <li>help</li>
        <li>icon</li>
        <li>licence</li>
        <li>next</li>
        <li>pingback</li>
        <li>prefetch</li>
        <li>prev</li>
        <li>search</li>
        <li>sidebar</li>
        <li>stylesheet</li>
        <li>tag</li>
	</ul>
</td>
<td>规定当前文档与被链接文档之间的关系。</td>
</tr>

<tr>
<td><a href="/tags/att_link_rev.asp" title="HTML <link> 标签的 rev 属性">rev</a></td>
<td><i>reversed relationship</i></td>
<td><span class="deprecated">HTML5 中不支持。</span></td>
</tr>

<tr>
<td class="html5_new"><a href="/tags/att_link_sizes.asp" title="HTML5 <link> sizes 属性">sizes</a></td>
<td>
	<ul>
	<li><i>heightxwidth</i></li>
	<li>any</li>
	</ul>
</td>
<td>规定被链接资源的尺寸。仅适用于 rel="icon"。</td>
</tr>

<tr>
<td><a href="/tags/att_link_target.asp" title="HTML <link> 标签的 target 属性">target</a></td>
<td>
	<ul>
	<li>_blank</li>
	<li>_self</li>
	<li>_top</li>
	<li>_parent</li>
	<li><i>frame_name</i></li>
	</ul>
</td>
<td><span class="deprecated">HTML5 中不支持。</span></td>
</tr>

<tr>
<td><a href="/tags/att_link_type.asp" title="HTML5 <link> type 属性">type</a></td>
<td><i>MIME_type</i></td>
<td>规定被链接文档的 MIME 类型。</td>
</tr>
</tbody></table>

'''

lines=[]

soup=BeautifulSoup(html_str,"lxml")



def get_lines_num():
    num = len(soup.find('tr').find_all('th'))
    if num==0:
        num = len(soup.find('tr').find_all('td'))
    return num

def create_md_title(num):
    line_1=''

    line = '|'
    for th in soup.find('tr').find_all('th'):
        if len(soup.find('tr').find_all('th')) != 0:
            line += ' ' + th.get_text() + ' |'
    if line != '|':
        line_1 = line.replace('\n', '')
        lines.append(line_1)
    else:
        line_1=('     ').join('|'*(num+1))
        lines.append(line_1)

    line_2=(' --- ').join('|'*(num+1))

    lines.append(line_2)



def get_main_body():

    for tr in soup.find_all('tr'):
        line = '|'
        for td in tr.find_all('td'):
            if len(tr.find_all('td')) != 0:
                if td.find('ul') != None:
                    ul_str=''
                    for li in td.find('ul').find_all('li'):
                        ul_str+=' '+li.get_text()
                    line += ' ' + ul_str + ' |'
                else:
                    line += ' ' + td.get_text() + ' |'
        if line != '|':
            line=line.replace('\n','')
            lines.append(line)


num=get_lines_num()

create_md_title(num)

get_main_body()

for line in lines:
    print(line)
