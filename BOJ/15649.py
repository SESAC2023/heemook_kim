# BOJ 15649번
from itertools import permutations

n, m = map(int, input().split())
arr = [_ for _ in range(1, n + 1)]

answer = [] 
answer.extend(permutations(arr, m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
