def func1():
    raise Exception("error is raise")

def func2():
    func1()

try:    
    func2()
except Exception as e:
    import traceback
    for frame in traceback.extract_tb(e.__traceback__): #<---- 1
        print("File: {}, Func: {}, Line: {}".format( frame.filename, frame.name, frame.lineno) )
