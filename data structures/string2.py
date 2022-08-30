# chr convert the integer to the character
x= chr(65)
print(x)
y= chr(2365)
print(y)
z= chr(12365)
print(z)

#ord convert the char in int
x= ord('A')
print(x)
y= ord('a')
print(y)
z= ord("{")
print(z)

# len show the length
print(len('amazing'))
print(len('world'))
size= len('hope')
print(size)


# adding string
a= 'apple'
b= 'juice'
ab= a+b
print(ab)
cd= a+' '+b # giving space
print(cd)

#word = 'Hi'
print( a* 3)

for i in range(6,0,-1):
    print(i*'*')

    
#rjust() for right alignment
for i in range(1,6):
    print((i*'+').rjust(35))
for i in range(5,0,-1):
    print((i*'+').rjust(35))
for i in range(1,15,2):
    print((i*'+').center(35))

for i in range(1,15,2):
    print((i*'*').center(35))
    if 
    for i in range(1,1):
        print((i*'o').center(35))
