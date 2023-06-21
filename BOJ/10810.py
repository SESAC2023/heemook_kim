# BOJ 10810번
n, m = map(int, input().split())

baskets = [[] for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        baskets[idx - 1].append(k)
        
[print(basket[-1], end=' ') if basket else print(0) for basket in baskets]
