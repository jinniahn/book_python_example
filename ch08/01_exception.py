print('Start')

try:
    print('processing #1')
    raise Exception("error is raise")   #<---- 1
    print('processing #2')              #<---- 2

except Exception:                       #<---- 3
    print('error is handled')           #<---- 4

else:                                   #<---- 5
    print('else state')                 #<---- 6

print('End')
