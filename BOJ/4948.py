# BOJ 4948번
import sys
input = sys.stdin.readline

def prime_num(limit):
    primes = [False] * (limit + 1) # 다이나믹 프로그래밍 활용하기 (문제에서 주어진 최대 범위에 대해서 미리 다 구해서 매번 구할 필요 없도록)
    
    for i in range(3, limit + 1, 2): # 짝수 제외하고 홀수만 체크
        for j in range(3, int(i ** 0.5) + 1, 2): # 제곱근까지만 확인 (짝수 제외했으니 마찬가지로 홀수로만 확인)
            if not i % j: # 하나라도 나누어 떨어지면
                break
        else: # 모든 j에 대해서 나누어 떨어지지 않았으면
            primes[i] = True

    return primes

limit = 123456 * 2 # 문제에서 주어진 최대 범위

primes = prime_num(limit) # 최대 범위의 소수 다 구해놓은 list

while True:
    n = int(input().rstrip())
    if not n:
        break
    if n == 1: # 1일 땐 범위가 [2:2]가 되므로 따로 구해주기
        answer = 1
    else:
        answer = sum(primes[n+1 : 2*n +1])
    print(answer)
