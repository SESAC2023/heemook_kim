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

visited = [False] * (n + 1)

selected = []

def backtracking(depth):
    if depth == m:
        for x in selected:
            print(x, end=' ')
        print()
        return    
    
    for i in range(1, n + 1):
        # if not visited[i]: # 순열에서 방문 정보를 삭제하므로써, 중복 허용
        #     visited[i] = True
            selected.append(i)
            backtracking(depth + 1)
            # visited[i] = False
            selected.pop()

backtracking(0)
