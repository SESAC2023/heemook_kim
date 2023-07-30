# BOJ 1746번
import sys
input = sys.stdin.readline

n, m = map(int ,input().split())

not_heard = []
for i in range(n):
    not_heard.append(input().rstrip())

not_seen = []
for j in range(m):
    not_seen.append(input().rstrip())

not_heard_seen = set(not_heard) - (set(not_heard) - set(not_seen))

result = list(not_heard_seen)
result.sort()

print(len(result))
for k in result:
	print(k)
