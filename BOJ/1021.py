# BOJ 1021번
from collections import deque

n, m = map(int, input().split())
queue = deque(_ for _ in range(1, n + 1))

target_list = deque(map(int, input().split()))

cnt = 0
while target_list:
    if target_list[0] == queue[0]:
        target_list.popleft()
        queue.popleft()
    else:
        idx = queue.index(target_list[0])
        if idx > len(queue) // 2:
            queue.rotate(1)
        else:
            queue.rotate(-1)
        cnt += 1
        
print(cnt)
