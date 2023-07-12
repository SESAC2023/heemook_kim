# BOJ 1037번
n = int(input())

약수 = list(map(int, input().split()))
약수.sort()

if len(약수) == 1:
    print(약수[0] ** 2)
else:
    print(약수[0] * 약수[-1])
