# index function

movies=['Ghostbuster: Afterlife','Spider-man: No way Home','Shang- chi','The lastduel']
flim= movies.index('Spider-man: No way Home')
print(flim)

#copy function copy the list in another list

fruits1=['apple','banana','guava']
fruits1.append('cherry')
dub=dup_fruit= fruits1.copy()
print(dub)
print(fruits1)

# clear function remove all element from the list

cl=fruits1.clear()
print(cl)

#pop function
#by list.pop()
v=fruits1.pop()
print(v)
#by list.pop(idx)
x=fruits1.pop(2)
print(x)