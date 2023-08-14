# BOJ 4134번
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def smallest_prime_num(n):
    """
    n보다 크거나 같은 소수 중 가장 작은 소수 찾기
    """
    if n <= 1 : # 0, 1이 주어지면
        return 2 # 2를 반환
    
    cnt = 0
    while True: # 2보다 큰 수에 대해서
        for i in range(2, int((n + cnt) ** 0.5) + 1): # 제곱근까지만 나눠보면 소수인지 판별할 수 있음
            if not (n + cnt) % i: # i로 나누어 떨어지면
                break
        else: # 모든 i에 대해서 나누어 떨어지지 않았으면
            return n + cnt
        
        cnt += 1

for _ in range(t):
    n = int(input())
    print(smallest_prime_num(n))
