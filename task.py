
from helper import read

data = read('pride_n_prejudice.txt')
def clean(dirty_data):
    from string import punctuation
    for p in punctuation:
        data=data.replace(p,'')
    return data
word = clean(data).lower().split()
#print(len('words'), 'unique'=,len(set(words)))
wordcount={}
for w in set (words):
    wordcount[w]=word.count(w)
return wordcount(word)