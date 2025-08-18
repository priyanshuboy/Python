import  os
import time

source = "test.txt"
destination = "E:\\python\\move.txt"

try :
    if(os.path.exists(destination)):
      print('file exists')
      time.sleep(5)
      os.remove(destination)
      print('file removed')
    else:
      os.replace(source,destination)
      print('file moved')

except FileNotFoundError as e:
    print(e)
    print('file not found')



