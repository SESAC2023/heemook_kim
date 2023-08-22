# BOJ 2108번
import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = []
cnt = [0] * 8001 # -4000부터 4000까지 정수 카운트 (문제 범위)
for _ in range(n):
    x = int(input().rstrip())
    arr.append(x)
    cnt[x + 4000] += 1 # 음수가 들어왔을 경우 ex) -2 -> 3998에 기록

arr = sorted(arr)
max_cnt = [i - 4000 for i in range(8001) if cnt[i] == max(cnt)] # 최빈값만 저장

# mean
print(round(sum(arr) / n))
# median
print(arr[n//2])
# mode
print(max_cnt[0] if len(max_cnt) == 1 else max_cnt[1])
# range (max - min)
print(arr[-1] - arr[0])
=======================================
# defaultdict를 이용해서 mode 구하는 방법
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

dictionary = defaultdict(int) # mode 카운트
for _ in range(n):
    x = int(input().rstrip())
    dictionary[x] += 1 # 카운트 + 1

max_cnt = max(dictionary.values())

max_cnts = []
for key, val in dictionary.items():
    if val == max_cnt:
        max_cnts.append(key)
max_cnts = sorted(max_cnts)

print(max_cnts[0] if len(max_cnts) == 1 else max_cnts[1])
