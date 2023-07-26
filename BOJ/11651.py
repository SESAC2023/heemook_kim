# BOJ 11651번
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())

coordinates = []
while n:
    x, y = map(int, input().split())
    heapq.heappush(coordinates, (y, x))
    n -= 1

while coordinates:
    y, x = heapq.heappop(coordinates)
    print(x, y)
