# BOJ 15650번
# from itertools import combinations
# n, m = map(int, input().split())
# arr = [_ for _ in range(1, n + 1)]

# answer = []
# answer.extend(combinations(arr, m))

# for i in answer:
#     for j in i:
#         print(j, end=' ')
#     print()
--------------------------------------
# BOJ 15650번
n, m = map(int, input().split())

visited = [False] * (n + 1)

selected = []

def backtracking(depth, now):
    if depth == m:
        for x in selected:
            print(x, end=' ')
        print()
        return    
    
    for i in range(now + 1, n + 1): # now 부터 시작하면 0부터 되므로 1부터로 맞춰주려고 now + 1
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            backtracking(depth + 1, i)
            visited[i] = False
            selected.pop()

backtracking(0, 0)
