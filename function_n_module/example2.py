def area():
    l=int(input('enter the length'))
    b=int(input('enter the breadth'))  
    area=l*b  
    print(f'{l}*{b}={area}')  

    return area

def  minmax():
    x=[31,43,54,234,56,34,23]
    return min(x), max(x) # return more then one value
#calling
print('area','area')
ans= area
print('area','ans')

ans= area()+area()+area()
print('total area',ans)
