# BOJ 1436번
# # 정답처리 되지만 너무 느림
# n = int(input())
# x = '666'
# 종말의수 = [i for i in range(666, 10000666) if str(i).count(x) >= 1]
# print(종말의수[n - 1])
-----------------------
n = int(input())
target = 666
while n:
    if '666' in str(target):
        n -= 1
    target += 1

print(target - 1)
