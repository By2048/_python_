import fire


class Calculator:

    def __init__(self):
        self.result = 0
        self.express = '0'

    def __str__(self):
        return f'{self.express} = {self.result}'

    def add(self, x):
        self.result += x
        self.express = f'{self.express}+{x}'
        return self

    def sub(self, x):
        self.result -= x
        self.express = f'{self.express}-{x}'
        return self

    def mul(self, x):
        self.result *= x
        self.express = f'({self.express})*{x}'
        return self

    def div(self, x):
        self.result /= x
        self.express = f'({self.express})/{x}'
        return self


if __name__ == '__main__':
    fire.Fire(Calculator)

"""

(_python_) E:\Git\_python_> python _package_\_fire_\calc.py add 1 sub 2 mul 3 div 4

"""
