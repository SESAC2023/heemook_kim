# BOJ 10811번
n, m = map(int, input().split())
basket = [0] + [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    basket[i : j + 1] = basket[j : i - 1 : -1]

basket.pop(0)
[print(_, end=' ') for _ in basket]
