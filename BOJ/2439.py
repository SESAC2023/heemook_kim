# BOJ 2439번
n = int(input())

for _ in range(1, n + 1):
    print(' ' * (n - _) + '*' * _)
