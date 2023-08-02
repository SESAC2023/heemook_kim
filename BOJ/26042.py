# BOJ 26042번
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

a = []
for i in range(n):
    info = tuple(map(int, input().split()))
    a.append(info)

# print(a)

b = deque() # 대기열 순서
c = [] # (대기열 길이, 대기열 순서)
max_len = 0
for j in range(len(a)):
    if a[j][0] == 1:
        b.append(a[j][1])
    if a[j][0] == 2:
        if a[j - 1][0] == 1: # 연속해서 학생을 들여 보내는 경우, max 가 될 수 없음 => 따라서 바로 전에는 학생이 줄을 섰고 이번에 들여 보내는 경우만 확인하면 됨
            max_len = max(max_len, len(b))
            c.append((len(b), b.copy()))
        b.popleft()
    elif j == len(a) - 1: # 마지막까지 줄만 계속 서는 경우가 줄이 제일 길 수도 있으므로 확인해야 됨
        max_len = max(max_len, len(b))
        c.append((len(b), b.copy()))

# print(c)
# print(max_len)

min_num = int(1e5)
for i in c:
    if i[0] == max_len:
        min_num = min(min_num, i[1][-1])

print(max_len, min_num)
