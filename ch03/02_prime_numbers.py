for n in range(2, 10):

    if n != 2 and n % 2 == 0: 
        continue                #<---- 1

        for x in range(2,n):
            if n % x == 0: 
                break           #<---- 2 
    else: 
        print('{}는 소수임'.format(n))
