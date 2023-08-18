# BOJ 17103번
def is_prime(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    """
    에라토스테네스의 체: 전체 범위에서 배수 지워나가기
    """
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i): 
            # i의 배수 지워나가기 ex) i = 3이면 9부터 [9, 12, 15 ...] => False
            # i * i부터 시작하는 이유 ex) i = 5의 경우, i = [2, 3]일 때 이미 [20, 15, 10]은 지워지기 때문에 i * [(i - 1), (i - 2), (i - 3) ...] 는 할 필요가 없음
                primes[j] = False
    return primes

limit = int(1e6)
primes = is_prime(limit)

t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0
    for i in range(2, n // 2 + 1): # 순서만 다른 경우 같은 파티션이므로 ex) n = 10인 경우 (3, 7), (5, 5)까지만 보면 됨  (7, 3)은 볼 필요 X
        if primes[i] and primes[n - i]: 
        # 인덱스 자체가 숫자를 나타내므로 i + (n - i)는 당연히 n이 됨 
        # 따라서 primes[i] 와 primes[n - i]가 소수인지만 판별하면 됨
            cnt += 1
    
    print(cnt)
