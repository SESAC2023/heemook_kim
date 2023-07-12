# BOJ 10872번
n = int(input())

answer = 1
while n:
    answer *= n    
    n -= 1

print(answer)
