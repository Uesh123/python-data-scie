# def word_counter(s):
#     word=s.split()
#     return len(word)
# print ('this is the example')


# def area(l,b):
#     l=int(input('enter the length'))
#     b=int(input('enter the breath'))
    
# def circumference(r):
#     r=int (input('enter the radius'))
#     return 2*3.14*r

# a=int(input('enter the length'))
# b=int(input('enter the breath'))
# o=area(a,b)
# print(o)


# #wap to calculate the sum of all the pime number frome 2 to 2000
# def prime():

#     n=[]
#     sum=0
#     m=int(input('enter the range'))
#     for i in range(2,m+1):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             n.append(i)
#             sum=sum+i
    
#     print(n)
#     print(sum)
# prime()


#WAP to remove all the punctuation from the string and return clean string
def punction():
    from string import punctuation
    n=input("enter the sentence")
    for p in punctuation:
        n=n.replace(p,'')
    print(n)
punction()

# wap to remove all the duplicate number from a two list and then return a single list of a unique number
 