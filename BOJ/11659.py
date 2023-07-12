# BOJ 11659번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
sum_arr = [0] * (n + 1)
result = 0
for i in range(1, n + 1): # 다이나믹 프로그래밍 처럼 누적합을 미리 계산해 둔다.
    result += arr[i - 1]
    sum_arr[i] = result

# print(sum_arr)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i - 1]) # dp 테이블에서 두 값만 가져와서 계산 => 속도 업!
