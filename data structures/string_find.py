# find and index are similar

msg = 'this is the place to find the answers related to coding'
print(msg.find('place'))
print(msg.find('palace')) # -1 means word not found
val= msg.find('answer')
if val==-1 :
    print('word not found')
else:
    print(f'word found at {val} index')


print(msg.find('is'))
print(msg.index('is'))
print(msg.find('is',5))