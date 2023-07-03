# BOJ 18258번
import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
        
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)