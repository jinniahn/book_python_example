import io
f = io.StringIO( ) 
f.write('2016-05-01\n') 
f.write(' - [ ] 책읽기\n') 
f.write(' - [ ] 커피한잔\n') 
f.write(' - [ ] 회의\n') 

# getvalue()로 출력한 내용을 볼 수 있음
print(f.getvalue( ))
f.close( )
