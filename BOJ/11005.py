# BOJ 11005번
n, b = map(int, input().split())

highest_degree = 0
while b ** highest_degree <= n:
    highest_degree += 1
highest_degree -= 1 # 최고차수 구하고

quotient = []
for i in range(highest_degree, -1, -1): # 차수돌아가면서 몫 넣어주고
    quotient.append(n // (b ** i))
    n %= (b ** i)
# print(quotient)

dic = dict()
for i in range(10): # 0~10까지 n진법 매핑
    dic[i] = str(i)
for i in range(10, 36): # A~Z까지 매핑
    dic[i] = chr(55 + i)
# print(dic)

for i in quotient:
    print(dic[i], end='')
