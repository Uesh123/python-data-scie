# indexing
str = 'digipodium'
print('str = ', str)

#first chara
print('str[0] = ', str[0])
#second char
print('str[1] = ', str[1])
#third char
print('str[-1] = ', str[-1])
#second last 
print('str[-2] = ', str[-2])

#sliceing
slice1= str[-9:7] #do't inclue last character of the ratio
slice2= str[:3]
print(slice1)
print(slice2)
slice3= str[4:len(str)] #or[4:]
print(slice3)

#reverse
rev_name = str[::-1]
print(rev_name)
#middal name reverse
name= 'umesh kumar maurya'
mname_rev= name[6:-7][::-1]
print(mname_rev)
#odd even index print
even_name = name[::2]
odd_name = name[1::2]
print(odd_name)
sclice= str[::-1]
print(sclice)