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

visited = [False] * (n + 1)

selected = []

def backtracking(depth):
    if depth == m:
        for x in selected:
            print(x, end=' ')
        print() # 간단하게 줄 바꾸는 방법
        return    
    
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            backtracking(depth + 1)
            visited[i] = False
            selected.pop() # 재귀를 마치고 다시 진행되기 때문에 append 된 숫자는 결국 전부 pop 된다!!

backtracking(0)
