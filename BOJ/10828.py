# BOJ 10828번
import sys
from collections import deque
input = sys.stdin.readline

num_input = int(input())

arr = deque()

for _ in range(num_input):
    command = input().split()
    if command[0] == 'push':
        arr.append(command[1])
        
    elif command[0] == 'pop':
        if arr:
            pp = arr.pop()            
            print(pp)
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(arr))
        
    elif command[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
        
    elif command[0] == 'top':
        if arr:
            print(arr[-1])
        else:
            print(-1)
