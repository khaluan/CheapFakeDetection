from config import *
from os import listdir, remove, stat
from os.path import isfile, join

filenames = [join(CONTEXT_DIR, f) for f in listdir(CONTEXT_DIR) if isfile(join(CONTEXT_DIR, f))]   
for filename in filenames:
    try:
        if stat(filename).st_size == 0:
            remove(filename)
        with open(filename, 'r', encoding='utf8') as file:
            content = eval(file.read())
            if content == {'heading': '', 'caption': '', 'context':''}:
                remove(filename)
    except Exception as e:
        print(e)
        print(filename)