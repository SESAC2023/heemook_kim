# BOJ 2581번
m = int(input())
n = int(input())

arr = [_ for _ in range(m, n + 1)]

def 소수찾기(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 1:        
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

소수 = []
for i in arr:
    if 소수찾기(i):
        소수.append(i)
if 소수:
    print(sum(소수))
    print(min(소수))
else:
    print(-1)
