# BOJ 11399번
import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()

answer = 0
for i in range(n):
    answer += (n - i) * time[i]

print(answer)
