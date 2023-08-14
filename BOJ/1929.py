# BOJ 4134번
n, m = map(int, input().split())

def smallest_prime_num(n, m):
    """
    n이상 m이하 소수 찾기
    """
    cnt = 0
    
    while n + cnt <= m: # n <= m 동안 1씩 더하면서 살펴보기
        if n + cnt == 1: # 1인 경우
            cnt += 1 # 1은 소수가 아니므로 2부터 시작
            pass
        for i in range(2, int((n + cnt) ** 0.5) + 1): # 제곱근까지만 나누어 보면 소수인지 판별 가능
            if not (n + cnt) % i: # i로 나누어 지면
                break # 소수가 아님
        else: # 모든 i에 대해서 나누어 지지 않았다면
            print(n + cnt) # 소수임
        
        cnt += 1
    
    return

answer = smallest_prime_num(n, m)
