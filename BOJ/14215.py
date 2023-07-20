# BOJ 14215번
lines = list(map(int, input().split()))
lines.sort()
a, b, c = lines[0], lines[1], lines[2]

while c >= a + b:
    c -= 1

print(a + b + c)
