from datetime import datetime
import time

print(1, datetime.fromtimestamp(1273969203.1234))
print(2, datetime.utcfromtimestamp(1273969203.1234))
print(3, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(4, datetime.strptime('2016-08-26', '%Y-%m-%d'))
print(5, time.mktime(datetime.now().timetuple()))
print(6, time.strftime('%Y-%m-%d', time.localtime(datetime.now().timestamp())))
