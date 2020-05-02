from datetime import datetime

from dateutil.relativedelta import relativedelta

"""
https://pypi.org/project/python-dateutil/
"""


def test_1():
    today = datetime.now()
    print(today)
    print(today + relativedelta(years=-1))
    print(today + relativedelta(months=1))


if __name__ == '__main__':
    test_1()
