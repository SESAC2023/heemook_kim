# BOJ 15649번
# from itertools import permutations

# n, m = map(int, input().split())
# arr = [_ for _ in range(1, n + 1)]

# answer = [] 
# answer.extend(permutations(arr, m))

# for i in answer:
#     for j in i:
#         print(j, end=' ')
#     print()
-------------------------------------
# BOJ 15649번
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
        if visited[j]:
            continue
        visited[j] = True
        selected.append(arr[j])
        backtracking(depth + 1)
        visited[j] = False
        selected.pop() # 재귀를 마치고 다시 진행되기 때문에 append 된 숫자는 결국 전부 pop 된다!!

backtracking(0)
