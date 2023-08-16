# BOJ 13909번
"""
[아이디어]
처음엔 모두 닫혀있지만, 모든 수가 1의 배수이므로 all True로 시작
windows = [False] + [True] * n

창문이 열려 있으면 True
창문이 닫혀 있으면 False
=> sum(windows) 하면 되겠다!

2 => False
3 => False
4 => 2의 배수일 때 False, 4일 때 True
5 => False
6 => 2의 배수일 때 False, 3의 배수일 때 True, 6일 때 False
7 => False
8 => 2의 배수일 때 False, 4의 배수일 때 True, 8일 때 False
9 => 3의 배수일 때 False, 9일 때 True,
10 => 2의 배수일 때 False, 5의 배수일 때 True, 10일 때 False

즉, 약수의 개수가 홀수이면 False / 약수의 개수가 짝수이면 True

결론: 약수의 개수가 짝수인 경우만 구하면 됨 
      => 제곱근 존재하는 경우
"""
n = int(input())

cnt = 0
for i in range(1, int(2100000000 ** 0.5) + 1): # 문제에서 주어진 최대 범위까지 순회하면서
    if i ** 2 > n:
        break
    cnt += 1 # 제곱근 개수 세기

print(cnt)
==========================
# 다른 사람 풀이
n=int(input())
print(int(n**0.5)) 
# 이렇게만 해도 제곱근 개수를 나타냄
# 왜냐면 제곱근 자체가 제곱근 개수를 나타냄 
# ex) 16까지 제곱근은 [1, 2, 3, 4], 즉 16의 제곱근인 4까지 당연히 4개가 존재
