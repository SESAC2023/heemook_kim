# BOJ 11404번
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 다익스트라와 달리 2차원 그래프 자체에 갱신

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y: # 자기 자신을 거치는 경우 거리는 0
            graph[x][y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # 경로가 1개가 아닐 수 있다는 조건이 있으므로, 항상 최단 경로를 선택하기 위해

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # k 를 거쳐가는 경로와 비교해서 최단 경로 갱신

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if graph[x][y] == INF:
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()
