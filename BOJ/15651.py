# BOJ 15651번
from itertools import product

n, m = map(int, input().split())

arr = [_ for _ in range(1, n + 1)]

answer = []
answer.extend(product(arr, repeat = m)) # 만약 repeat = m 이 아닌 m 만 적으면 arr 요소들과 m 이라는 단일 요소로 이루어진 조합을 생성

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
