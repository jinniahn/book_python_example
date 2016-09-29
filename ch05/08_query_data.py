import sqlite3
conn = sqlite3.connect('student.db')

sql = 'select * from student'
c = conn.cursor()
c.execute(sql)

# 하나의 데이터만
print(c.fetchone())

# 10개의 데이터를
for s in c.fetchmany(10):
    print(s)

for s in c.fetchall():
    print(s)
