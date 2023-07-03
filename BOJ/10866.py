# BOJ 10866번
import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    command = input().split()
    
    if command[0] == 'push_front':
        arr.insert(0, command[1])
    
    elif command[0] == 'push_back':
        arr.insert(len(arr), command[1])
    
    elif command[0] == 'pop_front':
        if arr:
            ppf = arr.pop(0)
            print(ppf)
        else:
            print(-1)
            
    elif command[0] == 'pop_back':
        if arr:
            ppb = arr.pop(-1)
            print(ppb)
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(arr))
        
    elif command[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    
    elif command[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
            
    elif command[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
