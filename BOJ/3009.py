# BOJ 3009번
width = []
height = []
for i in range(3):
    w, h = map(int, input().split())
    width.append(w)
    height.append(h)

for i in range(3):
    if width.count(width[i]) == 1:
        print(width[i], end=' ')
for i in range(3):
    if height.count(height[i]) == 1:
        print(height[i])
