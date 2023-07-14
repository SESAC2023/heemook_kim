# BOJ 2903번
n = int(input())

# 한 변이 2배씩 늘어나니까, 총 2의 제곱으로 증가
dp = [2 ** i for i in range(15)]

result = 2
for i in range(n):
    result += dp[i]

print(result ** 2)
