# BOJ 2751번
import sys
input = sys.stdin.readline
N = int(input())

result = []
while N > 0:
    x = int(input())
    result.append(x)
    N -= 1

result.sort()
for i in result:
    print(i)
