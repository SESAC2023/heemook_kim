# BOJ 20920번
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

voca = defaultdict(int)
for _ in range(n):
    x = input().rstrip()
    if len(x) >= m:
        voca[x] += 1

voca = sorted(voca.items(), key=lambda x: (-x[1], -len(x[0]), x[0])) # 1) value값이 클 수록 2) key의 길이가 길 수록 3) key의 알파벳 순서로

[print(i[0]) for i in voca]
