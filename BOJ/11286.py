# BOJ 11286번
import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip())

hq = []
for i in range(n):
    x = int(input().rstrip())
    if not x:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(x), x)) # 힙은 자동으로 첫 번째 원소값 기준, 두 번째 원소값 기준 순서로 정렬하기 때문에 절대값 원소와 원래 값을 둘 다 넣어주면 됩니다잇~!
