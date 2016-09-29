def func1():
    raise Exception("error is raise")

def func2():
    func1()

func2()
