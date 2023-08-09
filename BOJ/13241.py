# BOJ 13241번
a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

for i in range(1, a + 1):
    if not (b * i) % a:
        print(b * i)
        break
