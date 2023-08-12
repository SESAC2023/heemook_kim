# BOJ 2485번
from math import gcd
n = int(input())

# 가로수 정보
trees = [int(input()) for _ in range(n)]

# 가로수 사이 거리 정보
dist = [trees[i + 1] - trees[i] for i in range(n - 1)]

# 거리 정보들을 돌면서 최대 공약수를 구함
final_gcd = gcd(dist[0], dist[1])
for i in range(2, n - 1):
    final_gcd = gcd(final_gcd, dist[i])

# 최대 공약수로 나눈 거리마다 심어야 될 나무 세기
cnt = 0
for i in dist:
    cnt += i // final_gcd - 1

print(cnt)
