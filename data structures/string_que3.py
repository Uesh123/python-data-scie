# wap to remve all the punctuation from the string
str='this is ,that and that!and that is this, that is that ,and this is this' 
from string import punctuation
for p in punctuation:
    str=str.replace(p,'')
print(str)