# BOJ 11279번
import heapq
import sys
input = sys.stdin.readline

hq = []

for i in range(int(input().rstrip())):
    x = int(input().rstrip())
    if not x:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
            
    heapq.heappush(hq, -x)
