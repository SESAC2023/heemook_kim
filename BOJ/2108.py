# BOJ 2108번
import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = []
cnt = [0] * 8001 # -4000부터 4000까지 정수 카운트
for _ in range(n):
    x = int(input().rstrip())
    arr.append(x)
    cnt[x + 4000] += 1 # 음수가 들어왔을 경우 ex) -2 -> 3998에 기록

arr = sorted(arr)
max_cnt = [i - 4000 for i in range(8001) if cnt[i] == max(cnt)] # 최빈값만 저장

# mean
print(int(round(sum(arr) / n, 0)))
# median
print(arr[n//2])
# mode
print(max_cnt[0]) if len(max_cnt) == 1 else print(max_cnt[1])        
# range (max - min)
print(arr[-1] - arr[0])
