# BOJ 13305번
import sys
input = sys.stdin.readline

n = int(input().rstrip())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = dis[0] * price[0]
min_price = price[0]
cnt = 1
while cnt < (n - 1):
    if price[cnt] < min_price:
        min_price = price[cnt]
    answer += min_price * dis[cnt]
    cnt += 1

print(answer)
