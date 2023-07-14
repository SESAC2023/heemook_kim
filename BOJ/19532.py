# BOJ 19532번
a, b, c, d, e, f = map(int, input().split())

x = int(((e * c) - (b * f)) / ((e * a) - (b * d)))
y = int(((d * c) - (a * f)) / ((d * b) - (a * e)))

print(x, y)
