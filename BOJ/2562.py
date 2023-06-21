# BOJ 2562번
a = [int(input()) for i in range(9)]
print(max(a), a.index(max(a))+1, sep='\n')
