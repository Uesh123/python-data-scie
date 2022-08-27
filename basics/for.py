x= 'PYTHON'
for i in x:
    print (i)
#continue
for i in range(1,11):
    if (i==9):
        continue
    else:
        print(i)
#break
for i in range(1,11):
    if (i==9):
        print("out of loop")
        break
    else:
        print(i)

#for else
fruits = ['apple', 'banana','lemon']
for item in fruits:
    print(f'the fruit are {item}')
else:
    print("thats all ")