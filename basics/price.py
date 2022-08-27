n = int(input('enter the amount'))
pm = (input("payment method(credit, cash)"))
if n>1000:
   n -= n * 0.03
   print('cash final amount', n)
   
if pm == 'credit':
    n = n-100

n += n* .18 # tax 18%
print('final Amount',n)
print ('amount paid')
