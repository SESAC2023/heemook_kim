# BOJ 12789번
from collections import deque

n = int(input())

queue = deque(map(int, input().split()))
stack = []
order = 1
order_reverse = n
while queue:
    if queue[0] == order:
        queue.popleft()
        order += 1
        pass
    elif stack:
        if stack[-1] == order:
            stack.pop()
            order += 1
        else:
            stack.append(queue[0])
            queue.popleft()
    else:
        stack.append(queue[0])
        queue.popleft()
if stack == sorted(stack, reverse=True):
    print("Nice")
else:
    print("Sad")
