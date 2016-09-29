f = open('todo.txt', 'r+')
f.seek(16, 0)
f.write('X')
f.close
