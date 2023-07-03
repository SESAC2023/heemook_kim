# BOJ 15650번
from itertools import combinations
n, m = map(int, input().split())
arr = [_ for _ in range(1, n + 1)]

answer = []
answer.extend(combinations(arr, m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
