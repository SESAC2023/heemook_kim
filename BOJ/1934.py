# BOJ 1934번
from math import lcm

t = int(input())

while t:
    a, b = map(int, input().split())
    answer = lcm(a, b)
    print(answer)    
    t -= 1
