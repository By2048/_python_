"""
输出日期之间的间隔
"""

from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)

for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))


p=float('nan')
print(p)
print(type(p))

print(1>float('nan'))
print(1<float('nan'))