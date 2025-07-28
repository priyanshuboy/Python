#dictioneries : a changeable , unordered collection of  unique  key : value  pairs fast because they use hashing
#allow us to access value quickly

dictionary = {'USA' : " Washington ", 'India' : 'New delhi' ,'china':'beijing'}

print(dictionary['India'])
print(dictionary.get('russia'))
print(dictionary.keys())
print(dictionary.values())
dictionary.update({'russia':'moscow'})
for key, value in dictionary.items():
    print(key, value)