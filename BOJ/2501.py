# BOJ 2501번
n, k = map(int, input().split())

m = []
for i in range(1, int(n ** 0.5) + 1): # 약수는 서로 짝이 있기 때문에 제곱까지만 해보면 된다
    if n % i == 0:
        m.append(i)
        m.append(n // i)

m = list(set(m))
m.sort()

try:
    print(m[k - 1])
except:
    print(0)
