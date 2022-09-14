# genrater function to print it should be used in loop

def getcubes(limit=10):
    for i in range(1, limit+1):     
        yield i**3
def prime(start=2,stop=10):
    for num in range(start, stop):
        for i in range(2,num):
            if num % i==0:
                break
        else:
            yield num
             
for p in prime(stop=100):
    print()
print(sum)
# for val in getcubes():
#     print(val)

# for val in getcubes(5):
#     print(val)