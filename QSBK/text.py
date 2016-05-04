# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE spider (name varchar(255), text varchar(2555),id integer primary key autoincrement)')
# cur.execute('select * from spider')
# for s in cur.fetchall():
#     print s[1]
#     print '---------'

conn.commit()
conn.close()
