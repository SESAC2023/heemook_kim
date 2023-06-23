# BOJ 2738번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rows = []
for _ in range(n * 2):
    arr = list(map(int, input().split()))
    rows.append(arr)
    
a = rows[:n]
b = rows[n:]

answer = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        answer[i][j] = str(a[i][j] + b[i][j])

[print(' '.join(_)) for _ in answer]
