# BOJ 26069번
import sys
input = sys.stdin.readline

n = int(input().rstrip())

dancer = set()
dancer.add("ChongChong")

for _ in range(n):
    a, b = input().split()
    
    if a in dancer or b in dancer:
        dancer.add(a)
        dancer.add(b)

print(len(dancer))
