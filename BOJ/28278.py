# BOJ 28278번
import sys
input = sys.stdin.readline

n = int(input().rstrip())

stack = []
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    if cmd[0] == 2:
        if stack:
            top = stack.pop()
            print(top)
        else:
            print(-1)
    if cmd[0] == 3:
        print(len(stack))
    if cmd[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    if cmd[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
