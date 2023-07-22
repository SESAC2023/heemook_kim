# BOJ 2839번
n = int(input())

min_val = int(1e6)
for i in range((n // 5) + 1):
    target = n
    target -= 5 * i # 5의 배수씩 빼가면서 모든 경우의 수 해보기 (브루트 포스)
    cnt = i
    if not target % 3:
        cnt += target // 3
        min_val = min(min_val, cnt)
    else:
        continue

if min_val == int(1e6):
    print(-1)
else:
    print(min_val)
