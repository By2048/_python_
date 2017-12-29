import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

#基本用法
a = markdown.markdown("*boo!*")
b = markdown.markdown("**boom!**")
print(a)
print(b)

#扩展用法
input_file = open("foo.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text, output_format='html5', \
    extensions=['markdown.extensions.toc',\
    WikiLinkExtension(base_url='https://en.wikipedia.org/wiki/',\
        end_url='#Hyperlinks_in_wikis'),\
    'markdown.extensions.sane_lists',\
    'markdown.extensions.codehilite',\
    'markdown.extensions.abbr',\
    'markdown.extensions.attr_list',\
    'markdown.extensions.def_list',\
    'markdown.extensions.fenced_code',\
    'markdown.extensions.footnotes',\
    'markdown.extensions.smart_strong',\
    'markdown.extensions.meta',\
    'markdown.extensions.nl2br',\
    'markdown.extensions.tables'])


output_file = open("foo.html", "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
)
output_file.write(html)