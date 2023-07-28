# BOJ 14425번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input().rstrip())

cnt = 0
for j in range(m):
    t = input().rstrip()
    if t in s:
        cnt += 1

print(cnt)
