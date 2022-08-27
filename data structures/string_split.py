msg= ('He is the superhuman as a computer')

word= msg.split() # split function
print(word,len(word),'word found')

word= msg.split(',')
print(word,len(word),'word found')

word= msg.split('is')
print(word,len(word),'word found')


word=(msg.split()[-1])
print(word)
 