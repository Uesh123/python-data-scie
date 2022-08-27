# wap to count all the characters in a string

str= "wap to count all the characters in a string"
val=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # import ascii_lowercase
for i in val:
    count= str.count(i)
    print(f'{i} - {count}')



# wap to find the occuranc of a word in a sting and display its index

str1= 'this is that and that and that is this, that is that and this is this'
chr= str1.find('this')
print(chr)
