"""
https://pythonhosted.org/Pympler/
"""


class obj(object):
    def __init__(self):
        self.memory = str(id(self)) * 2 ** 10


my_str = 'a' * 2 ** 26
my_objs = [obj() for _ in range(2 ** 16)]


def memory_summary():
    from pympler import summary, muppy
    mem_summary = summary.summarize(muppy.get_objects())
    rows = summary.format_(mem_summary)
    return '\n'.join(rows)


print(memory_summary())
