try:
    # 테스트를 위해 파일 생성
    open('__test.txt', 'w').close()

    # 파일을 읽기로 연다. 
    f = open('__test.txt','r')
    # 파일에 뭔가를 쓰면 예외
    f.write('xxx')            
except OSError as e:          
    print('Exception: {}'.format(e))

finally:                           #<---- 1
    f.close()                      #<---- 2
    print('release file')
