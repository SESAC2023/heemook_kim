# BOJ 11047번
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

money = reversed([int(input().rstrip()) for _ in range(n)])

cnt = 0

while k:
    for i in money:
        if i > k:
            continue
        else:
            cnt += k // i
            k %= i
        if k == 0:        
            break

print(cnt)
