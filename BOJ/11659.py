# BOJ 11659번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + arr[i - 1] # 점화식으로 나타낼 수 있다 => 다이나믹 프로그래밍 (누적합을 미리 계산해 두기)

# print(dp)

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1]) # dp 테이블에서 두 값만 가져와서 계산 => 속도 업!
