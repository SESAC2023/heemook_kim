# BOJ 1620번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

poket = dict()
for i in range(1, n+1):
	mon = input().rstrip()
	poket[str(i)] = mon

inverted_poket = {val:key for key, val in poket.items()} # key:value -> value:key 뒤집기

야생의포켓몬 = []
for j in range(m):
	야생의포켓몬.append(input().rstrip())

for k in 야생의포켓몬:
	if k in poket.keys():
		print(poket[k])
	if k in inverted_poket.keys():
		print(inverted_poket[k])
