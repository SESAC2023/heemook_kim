# BOJ 2292번
"""
1: 1, 1 + 6 * 0
2: 2~7, 1 + 6 * 1
3: 8~19, 1 + 6 * (1 + 2)
4: 20~37, 1 + 6 * (1 + 2 + 3)
5: 38~61, 1 + 6 * (1 + 2 + 3 + 4)
6: 62     1 + 6 * (1 + 2 + 3 + 4 + 5)
"""
n = int(input())
x = (n - 1) // 6
y = int((1 + (1 + 8 * x) ** 0.5) // 2 + 1)

factors = [_ for _ in range(y)]
누적합 = [0] * len(factors)
for i in range(1, len(factors)):
    누적합[i] = 누적합[i - 1] + factors[i]

print(누적합)

for idx, val in enumerate(누적합):
    if 1 + 6 * val >= n:
        print(idx + 1)
        break
