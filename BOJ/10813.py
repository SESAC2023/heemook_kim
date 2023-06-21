# BOJ 10813번
n, m = map(int, input().split())

baskets = [[_] for _ in range(1, n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    baskets[a - 1][0], baskets[b - 1][0] = baskets[b - 1][0], baskets[a - 1][0]

[print(_[0], end=' ') for _ in baskets]
