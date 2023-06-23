# BOJ 2444번
n = int(input())
for i in range(1, n+1):
    line = ' '*(n-i) + '*'*(2*i-1)
    print(line)
    
for j in range(n-1, 0, -1):
    line = ' '*(n-j) + '*'*(2*j-1)
    print(line)
