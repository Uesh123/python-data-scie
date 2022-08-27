# wap to find the occuranc of a word in a sting and display its index

str= 'this is that and that and that is this, that is that and this is this'
start= 0
chr='that'
while True :
    idx=str.find(chr, start)
    if idx==-1:
        break
    print(f'{chr} at {idx}')
    start=idx+1