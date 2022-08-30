#Append is function to add the any thing at the last in list

fruits=[]
fruits.append('apple')
fruits.append('banana')
fruits.append('cherry')
fruits.append('guava')
print(fruits)

#insert function is used to add object in the define position

fruits1=['apple','banana','guava']
dry_fruits=['Almond','cashew','walnut']
fruits1.insert(1, 'cherry')
# extend function merge second list in the first list
fruits1.extend(dry_fruits)
# sort function sort the list
fruits1.sort()
#remove function remove object from the list
fruits1.remove('cherry')
print(fruits1[::-1])

#count function
x=[1,2,3,4,5,6,7,8,9,1,2,3,4,3,2,]
num=x.count(1)
print(num)