try:
    # 테스트를 위해 파일 생성
    open('__test.txt', 'w').close()

    # 파일을 읽기로 연다. 
    f = open('__test.txt','r')    #<---- 1
    # 파일에 뭔가를 쓰면 예외
    f.write('xxx')                #<---- 2
    # 이 코드는 절대 실행안됨
    f.close()                     #<---- 3
except OSError as e:              #<---- 4
    print(e)
