# BOJ 1157번
from collections import Counter
word = input()
word = word.upper()
word = [i for i in word]
counter = Counter(word)

set_word = set(word)
results = []
for i in set_word:
    result = (i, counter[i])
    results.append(result)
    
results.sort(key = lambda x : x[1], reverse=True)

chk = results.pop(0)
if results:
    if results[0][1] == chk[1]:
        print('?')
        
    else:
        print(chk[0])
else:
    print(chk[0])
