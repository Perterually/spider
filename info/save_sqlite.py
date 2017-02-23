import sqlite3
import os
class SaveSQl():
    """save data function

    :param name: database name
    """
    def __init__(self,name):
        """init sqlite connn

        """
        self.create_db(name)
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()
        
    def insert(self, items):
        self.cur.executemany(
            'INSERT INTO info(name,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
            items)
        self.conn.commit()

    def create_db(self,name):
        """Create Database.
        
        : param : Database name
        """
        li = os.listdir()
        if name is li:
           os.remove(name)
        else:
            conn = sqlite3.connect(name)
            sql = 'CREATE TABLE info (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,name text(128),name1 text(128),name2 text(128),name3 text(128),name4 text(128),name5 text(128),name6 text(128),name7 text(128),name8 text(128),name9 text(128),name10 text(128),name11 text(128),name12 text(128),name13 text(128),name14 text(128),name15 text(128),name16 text(128),name17 text(128),name18 text(128),name19 text(128));'
            conn.execute(sql)
            print('Create Database successful')
    
    def close_conn(self):
        """Close connect

        """
        self.conn.close()



