# BOJ 1541번
import sys
input = sys.stdin.readline

eqn = input().rstrip()

# '-'로 쪼개고 나중에 총합에서 빼는 형식
minus = eqn.split('-')

# 처음 '-'가 나오기 전까지 나온 수들을 먼저 '+'로 쪼개고 다 더하기
answer = sum(map(int, minus[0].split('+')))

# '-'로 쪼갠 수들은 다 더한 후 '-'가 나오기 전까지 합한 수에서 빼기
for i in minus[1:]:
    x = sum(map(int, i.split('+')))
    answer -= x

print(answer)
