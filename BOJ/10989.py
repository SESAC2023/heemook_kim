# BOJ 10989번
import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input().rstrip())

cnt = [0] * 10001 # 계수 정렬을 사용하기 위해 입력 조건으로 주어진 자연수 전체 범위로 설정

for i in range(n):
    cnt[int(input())] += 1 # 해당 인덱스에 계수 추가

for i in range(10001):
    for j in range(cnt[i]):
        print(f'{i}\n')
