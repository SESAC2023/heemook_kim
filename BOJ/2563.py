# BOJ 2563번
n = int(input())
black = [tuple(map(int, input().split())) for _ in range(n)]

paper = [[False] * 100 for _ in range(100)]

for _ in black:
    x, y = _[1], _[0]
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = True

cnt = 0
for _ in paper:
    cnt += _.count(1)
    
print(cnt)
