# BOJ 2745번
import sys
input = sys.stdin.readline

arr = input().split()
n, b = arr[0][::-1], arr[1] # n 을 뒤집는 이유는 마지막부터 0승 -> 1승 -> 2승 순서기 때문

dic = dict()
for i in range(10): # 0 ~ 9 진법인 경우도 '문자'로 입력해 주어야 한다.
    dic[str(i)] = i

for i in range(10, 36): # A ~ Z 아스키 코드로 입력
    dic[chr(i + 55)] = i

answer = 0
for i in range(len(n)):
    answer += dic[n[i]] * (int(b) ** i)

print(answer)
