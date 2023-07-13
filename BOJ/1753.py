# BOJ 1753번
import sys
input = sys.stdin.readline

import heapq
INF = int(1e9) # 무한 설정

V, E = map(int, input().split()) # 노드, 간선 수
graph = [[] for _ in range(V + 1)] # 그래프 초기화

K = int(input().rstrip()) # 시작점

for i in range(E):
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w)) # u 에서 v 까지 거리는 w

distance = [INF] * (V + 1) # 거리 무한으로 초기화

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리가 우선 순위인 큐를 만들기 위해 (거리, 노드)
    distance[start] = 0 # 시작점에서 시작점까지 거리는 0
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: # 이미 최단 경로인 경우
            continue
        for i in graph[now]: # 현재 노드에 연결된 노드들을 순회
            cost = dist + i[1] # 비용: 현재 노드 + 간선 길이
            if cost < distance[i[0]]: # 비용이 더 짧은 경우 == 최단 경로를 갱신할 수 있는 경우
                distance[i[0]] = cost # 갱신
                heapq.heappush(q, (cost, i[0])) # 새로운 최단 경로를 갖고 다익스트라를 재수행하기 위해
                                                # i 는 heap 과 반대의 구조, (노드, 거리)

dijkstra(K) # 시작점이 K 인 다익스트라 수행 (K 부터 각 노드까지의 최단 경로를 알아내는 알고리즘)

for i in range(1, V + 1): # 1번 노드부터 각 노드까지의 거리 확인
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
