import re


def md_header(data):
    """ ## {...} """
    compile = re.compile(r"^(#{1,6})\s*(.*?)\s*$", re.M)

    def repl(match):
        tags = match.group(1)
        content = match.group(2)
        tag_start = '<h{}>'.format(len(tags))
        tag_end = '</h{}>'.format(len(tags))
        return tag_start + content + tag_end

    return compile.sub(repl=repl, string=data)


def md_emphasize(data: str):
    compile = re.compile(r"([*|_]{1,2})(.*)\1", re.DOTALL)

    def repl(match):
        tags = match.group(1)
        content = match.group(2)
        code = ''
        if len(tags) == 2:
            code = 'strong'
        elif len(tags) == 1:
            code = 'em'
        tag_start = '<{}>'.format(code)
        tag_end = '</{}>'.format(code)
        return tag_start + content + tag_end

    return compile.sub(repl=repl, string=data)


def test():
    print(md_header("## Data"))
    print(md_emphasize("**Data**"))
    print(md_emphasize("*Data*"))
