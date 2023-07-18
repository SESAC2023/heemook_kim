# BOJ 11050번
n, k = map(int, input().split())

x = 1
for i in range(n, n-k, -1):
    x *= i

y = 1
for j in range(k, 0, -1):
    y *= j

print(x//y)
