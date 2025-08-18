
try:
   denominator = int(input('value : '))
   numerator = int(input('value : '))
   result = numerator / denominator
   print(result)

except ZeroDivisionError:
    print('division by zero')
finally:
    print('finally')
