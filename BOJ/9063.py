# BOJ 9063번
import sys
input = sys.stdin.readline
n = int(input().rstrip())

x = []
y = []
for _ in range(n):
    u, v = map(int, input().split())
    x.append(u)
    y.append(v)

width = max(x) - min(x)
height = max(y) - min(y)

print(width * height)
