# BOJ 1085번
x, y, w, h = map(int, input().split())

width = min(x, abs(x - w))
height = min(y, abs(y - h))

answer = min(width, height)

print(answer)
