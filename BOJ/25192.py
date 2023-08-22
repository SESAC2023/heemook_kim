# BOJ 25192번
import sys
input = sys.stdin.readline

n = int(input().rstrip())

answer = 0 # 정답 숫자 세기 위해
while n: # n만큼 입력 받음
    logs = set() # ENTER 다음 중복된 아이디가 있는 경우 곰돌이 인사 후 다른 채팅이므로 제거해주기 위해
    for i in range(n):
        log = input().rstrip()
        n -= 1 # 앞으로 입력받을 숫자 -1
        if log == "ENTER": # ENTER마다 끊어서 보기 위해
            break
        logs.add(log)
    result = len(logs) # logs들 결과
    answer += result # 정답에 더해주기

print(answer)
