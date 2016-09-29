import sqlite3
conn = sqlite3.connect('student.db')
sql = '''
  INSERT INTO student VALUES
         (?, ?, ?)
'''
c = conn.cursor()   # 객체 생성
c.execute(sql, ('학생2', 2, '서울'))

data = [
    ('학생3', 3, '서울'),
    ('학생4', 4, '서울'),
    ('학생5', 5, '서울'),
]
c.executemany(sql, data)
c.close()
conn.commit()
