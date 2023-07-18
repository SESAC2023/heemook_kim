# BOJ 1018번
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]

def diff_cnt(x, y):
    """
    문자열에서 서로 다른 문자 수 반환하는 함수
    """
    cnt = 0
    for i, j in zip(x, y):
        if i != j:
            cnt += 1
    return cnt

a1 = 'WBWBWBWBBWBWBWBW' * 4 # 체스판 만드는 첫 번째 방법
a2 = 'BWBWBWBWWBWBWBWB' * 4 # 체스판 만드는 두 번째 방법
min_val = int(1e6)
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        chess = ''
        for k in range(8):
            chess += graph[i+k][j:j+8] # graph에서 좌표를 돌면서 새로운 8 x 8 체스판 만들기
        diff_min = min(diff_cnt(a1, chess), diff_cnt(a2, chess)) # 두 가지 경우 중에서 칠해야 하는 최소 네모칸 수
        min_val = min(min_val, diff_min) # 만들 수 있는 모든 좌표 중에서 최소 네모칸 수 갱신

if n == 8 and m == 8: # 8 x 8 의 경우만 따로 해주기
    chess = ''
    for i in graph:
        chess += i
    print(min(diff_cnt(a1, chess), diff_cnt(a2, chess)))
else:
    print(min_val)
  
