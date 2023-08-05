# BOJ 28279번
import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())

덱 = deque()
for _ in range(n):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        덱.appendleft(cmd[1])
    
    elif cmd[0] == 2:
        덱.append(cmd[1])
    
    elif cmd[0] == 3:
        print(덱.popleft() if 덱 else -1)
    
    elif cmd[0] == 4:
        print(덱.pop() if 덱 else -1)
        
    elif cmd[0] == 5:
        print(len(덱))
        
    elif cmd[0] == 6:
        print(1 if not 덱 else 0)
        
    elif cmd[0] == 7:
        print(덱[0] if 덱 else -1)
        
    elif cmd[0] == 8:
        print(덱[-1] if 덱 else -1)

# """
# 덱을 구현하는 문제라서 deque 를 사용하지 않고 싶었으나 시간 초과 뜸
# len 를 필요로 할 때마다 cnt 를 사용하여 간단하게 해결한 줄 알았으나 실패
# """
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())

# 덱 = []
# cnt = 0
# for _ in range(n):
#     cmd = list(map(int, input().rstrip().split()))
    
#     if cmd[0] == 1:
#         덱.insert(0, cmd[1])
#         cnt += 1
    
#     elif cmd[0] == 2:
#         덱.append(cmd[1])
#         cnt += 1
    
#     elif cmd[0] == 3:
#         print(덱.pop(0) if cnt else -1)
#         cnt -= 1
    
#     elif cmd[0] == 4:
#         print(덱.pop() if cnt else -1)
#         cnt -= 1
        
#     elif cmd[0] == 5:
#         print(cnt)
        
#     elif cmd[0] == 6:
#         print(1 if not cnt else 0)
        
#     elif cmd[0] == 7:
#         print(덱[0] if cnt else -1)
        
#     elif cmd[0] == 8:
#         print(덱[-1] if cnt else -1)
