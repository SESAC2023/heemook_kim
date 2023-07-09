# BOJ 15652번
# from itertools import combinations_with_replacement

# n, m = map(int, input().split())

# arr = [_ for _ in range(1, n + 1)]

# answer = []
# answer.extend(combinations_with_replacement(arr, m))

# for i in answer:
#     for j in i:
#         print(j, end=' ')
#     print()
------------------------------------------------------
# BOJ 15652번
n, m = map(int, input().split())
arr = [_ for _ in range(1, n + 1)]
visited = [False] * n

selected = []

def backtracking(depth, now): # 조합
    if depth == m:
        for i in selected:
            print(i, end=' ')
        print()
        return
    
    for j in range(now, n):
        # if visited[j]: # 방문 처리 삭제 => 중복 허용
        #     continue
        # visited[j] = True
        selected.append(arr[j])
        backtracking(depth + 1, j)
        # visited[j] = False
        selected.pop()

backtracking(0, 0)
