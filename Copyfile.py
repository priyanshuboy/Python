#copyfile : copy all data from a file
#copy() : copyfile + permission mode + destination can be directory
#copy2() : copy() + copies metadata

import shutil

shutil.copyfile('test.txt', 'new.txt')
shutil.copy('test.txt', 'new.txt')
shutil.copy2('test.txt', 'new.txt')
with open('new.txt' ,'r') as file1:
    print(file1.read())

