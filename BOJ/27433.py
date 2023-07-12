# BOJ 27433번
import sys
sys.setrecursionlimit(int(1e9))

n = int(input())

dp = [0] * 20

dp[0] = 1
dp[1] = 1

def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x - 1)

print(factorial(n))
