import sqlite3

conn = sqlite3.connect('mynewsql.db')

cur = conn.cursor()

#cur.execute('CREATE TABLE STUDENT(SID INT,SNAME VARCHAR(20))')
cur.execute("UPDATE STUDENT SET SNAME='ICHIGO' WHERE SID=2")
conn.commit()