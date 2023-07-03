# BOJ 10814번
N = int(input())

info = []
for i in range(N):
    age, name = input().split()
    info.append((int(age), name))
    
info.sort(key=lambda x: x[0])
for j in info:
    print(j[0], end=' ')
    print(j[1])
