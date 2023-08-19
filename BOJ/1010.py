# BOJ 1010번
import sys
from math import comb
input = sys.stdin.readline

t = int(input().rstrip())

while t:    
    n, m = map(int, input().split())
    
    answer = comb(m, n)
    
    print(answer)
    
    t -= 1
====================================
# 백트래킹 => 시간 초과
import sys
sys.setrecursionlimit(int(1e9))
t = int(input())

while t:

    n, m = map(int, input().split())

    arr = [_ for _ in range(1, m + 1)]

    visited = [False] * m

    selected = []

    cnt = 0
    def combination_rep(depth, now):
        global cnt
        if depth == n:
            cnt += 1
            # for x in selected:
            #     print(x, end=' ')
            # print()
            return
        
        for i in range(now, m):
            if visited[i]:
                continue
            selected.append(arr[i])
            visited[i] = True
            combination_rep(depth + 1, i + 1)
            selected.pop()
            visited[i] = False

    combination_rep(0, 0)
    print(cnt)
    t -= 1
