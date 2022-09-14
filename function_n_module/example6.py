# from types import LambdaType
# lambda is used in map() our the filter()
#map() perform same operation on the every elemnt
# lambda a,b:a+b 

# adder=lambda a, b:a+b
# print(adder(69,225))

# def exp(power):
#     return lambda l : [a**power for a in l]
# four = exp(4)
# four([2,4,6,8,10])

from unicodedata import name


x=[2,3,4,5,6,7]
o=list(map(lambda i:i**2, x))
x5=list(map(lambda i:i-5,x))
print(o) # lazy output
print(x5)

#filter
y3=list(filter(lambda i:i>3,x))
print(y3)

name=['Raj Singh','Vijay Singh','Ravi kumar',
        'Ajay Singh','Raja kumar']
name_singh=list(filter(lambda n: n.endswith('Singh'),name))
print(name_singh)
name_a=list(filter(lambda n: n.startswith('A'),name))
print(name_a)


