# string slicing : - can be used to produce a substring from a string or extracting a substring from another string


name = 'priyanshu'

first_name = name[2:7] #indexing[]
second_name = name[::2]
print(second_name)
print(first_name)
website = "http://google.com"

Slice = slice(7,-4) #slice

print(website[Slice])