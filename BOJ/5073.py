# BOJ 5073번
import sys
input = sys.stdin.readline

while True:
    lines = list(map(int, input().split()))
    lines.sort()
    a, b, c = lines[0], lines[1], lines[2]
    
    if a == b and b == c and c == 0:
        break
    elif c >= a + b:
        print("Invalid")
    elif len(set(lines)) == 1:
        print("Equilateral")
    elif len(set(lines)) == 2:
        print("Isosceles")
    elif len(set(lines)) == 3:
        print("Scalene")
