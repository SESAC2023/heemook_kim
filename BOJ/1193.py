# BOJ 1193번
import sys
input = sys.stdin.readline

x = int(input().rstrip())

stage = 0
while x > 0: # 몇 단계인지
    stage += 1
    x -= stage

if stage % 2 == 0: # 짝수면
    분자 = stage + x
    분모 = (stage + 1) - 분자

else: # 홀수면
    분모 = stage + x
    분자 = (stage + 1) - 분모

print(f'{분자}/{분모}')
