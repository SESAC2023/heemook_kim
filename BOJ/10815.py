# BOJ 10815번
import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

n = int(input().rstrip())
cards = list(map(int, input().split()))
cards.sort()

m = int(input().rstrip())
valid = list(map(int, input().split()))

# [print(1, end=' ') if i in cards else print(0, end=' ') for i in valid]
# 시간 초과 뜨니까 -> 이분 탐색 슛~!

start = 0
end = len(cards) - 1
def binary_search(n, start, end):
    if start > end:
        print(0, end=' ')
        return 
    mid = (start + end) // 2
    if n == cards[mid]:
        print(1, end=' ')
        return
    elif n > cards[mid]:
        start = mid + 1
        binary_search(n, start, end)
    elif n < cards[mid]:
        end = mid - 1
        binary_search(n, start, end)
    return

for i in valid:
    binary_search(i, start, end)
