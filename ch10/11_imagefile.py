from os.path import splitext

def is_supported_files(filename):
    supported = ".png .jpg".split()

    name, ext = splitext(filename)
    return ext in supported


files = "test.png test.doc test.exe test.jpg".split()
for f in files:
    if is_supported_files(f):
        print("{} is allowed".format(f))
