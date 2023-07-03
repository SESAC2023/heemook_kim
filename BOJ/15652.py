# BOJ 15652번
from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = [_ for _ in range(1, n + 1)]

answer = []
answer.extend(combinations_with_replacement(arr, m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
