#sets : collection which is unordered ,unindexed and no duplicates value

utils = {'fork' , 'spoon','spa'}
dishes = {'bowl' , 'plate' ,'spa'}

new_data = utils.union(dishes)
print(utils.difference(dishes))
for x in new_data:
    print(x)


