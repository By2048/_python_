import sqlite3
import datetime
import time

conn=sqlite3.connect('F:\\_test\\test.db')

cur=conn.cursor()

# cur.execute('''
# create table has_down
# (
#     id              integer primary key autoincrement not null,
#     link            varchar not null,
#     title           nvarchar not null,
#     tag             nvarchar not null,
#     release_time    text not null,
#     browse_num      integer not null
# );
# ''')

for item in range(10):
    info=['link'+str(item),'title'+str(item),'tag'+str(item),time.time(),item]
    cur.execute("insert into has_down(link,title,tag,release_time,browse_num) values(?,?,?,?,?)",info)
conn.commit()

cur.execute("select * from has_down")
for item in cur.fetchall():
    print(item[0])
