# BOJ 2164번
N = int(input())

M = N
cnt = 0
while M // 2 != 0:
    M = M // 2
    cnt += 1
    
answer = N - (2 ** cnt)
if answer != 0:
    print(2 * answer)
else:
    print(2 ** cnt)
