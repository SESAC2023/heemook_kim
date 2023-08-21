# BOJ 24416번
n = int(input())

dp = [0] * (n + 1) # 다이나믹 프로그래밍
cnt = 0 # dp활용했을 때 호출 횟수
def fibo(n, dp):
    global cnt
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt += 1
    return cnt

fibo(n, dp)
print(dp[n], cnt) # dp[n] = n의 피보나치 수 = 재귀 사용했을 때 호출된 횟수
=======================================================================
n = int(input())

dp = [0] * (n + 1)

def fibo(n, dp):
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibo(n, dp), n)
