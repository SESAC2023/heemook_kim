# BOJ 1010번
import sys
input = sys.stdin.readline

t = int(input().rstrip())

while t:    
    n, m = map(int, input().split())
    """
    mCn 직접 구현
    """
    N = 1
    M = 1
    K = 1
    for i in range(1, m + 1):
        M *= i
    for j in range(1, n + 1):
        N *= j
    for k in range(1, m - n + 1):
        K *= k
    
    print(int(M/(N * K)))    
    t -= 1
====================================
# math 라이브러리 이용
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
