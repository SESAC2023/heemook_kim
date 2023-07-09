# BOJ 15651번
# from itertools import product

# n, m = map(int, input().split())

# arr = [_ for _ in range(1, n + 1)]

# answer = []
# answer.extend(product(arr, repeat = m)) # 만약 repeat = m 이 아닌 m 만 적으면 arr 요소들과 m 이라는 단일 요소로 이루어진 조합을 생성

# for i in answer:
#     for j in i:
#         print(j, end=' ')
#     print()
-----------------------------------------
# BOJ 15651번
n, m = map(int, input().split())
arr = [_ for _ in range(1, n + 1)]
visited = [False] * n

selected = []

def backtracking(depth):
    if depth == m:
        for i in selected:
            print(i, end=' ')
        print()
        return
    
    for j in range(n):
        # if visited[j]: # 순열에서 방문 정보를 삭제하므로써, 중복 허용
        #     continue
        # visited[j] = True
        selected.append(arr[j])
        backtracking(depth + 1)
        # visited[j] = False
        selected.pop()

backtracking(0)
