# BOJ 11866번
from collections import deque

N,M = map(int,input().split())

human = deque([i + 1 for i in range(N)])
result = '<'

i = 1 
count = 1

while len(human) >= 1:
    
    if i % M == 0:
        if count != N:
            result += str(human.popleft()) + ', '
        else:
            result += str(human.popleft()) + '>'
        i +=1 
        count += 1
    else:
        human.append(human.popleft())
        i += 1
        
print(result)
