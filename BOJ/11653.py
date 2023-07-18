# BOJ 11653
n = int(input())

인수 = 2
while n != 1:
    while not n % 인수:
        n //= 인수
        print(인수)
    인수 += 1
