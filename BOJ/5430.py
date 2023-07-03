# BOJ 5430번
from collections import deque

t = int(input())

while t:
    p = input()
    n = int(input())
    arr = deque(input()[1:-1].split(','))
    
    if n == 0:
        arr = []
        
    cnt = 0
    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if arr:
                if cnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if cnt % 2 == 1:
            arr.reverse()
        print('[' + ','.join(arr) + ']')
    
    t -= 1
