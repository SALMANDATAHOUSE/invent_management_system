import sqlite3

conn = sqlite3.connect('patient.db')

cur = conn.cursor()

#cur.execute('CREATE TABLE Patient(PID INT,PNAME VARCHAR(20),PAge INT)')
cur.execute("INSERT INTO Patient VALUES(4,'ASTA',24)")
conn.commit()