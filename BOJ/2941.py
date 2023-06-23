# BOJ 2941번
# import sys
# input = sys.stdin.readline

변경 = input()
크로아티아 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
for i in 크로아티아:
    if i in 변경:
        cnt += 변경.count(i)
        변경 = 변경.replace(i, ' ')
        
a= ''
for i in 변경.split():
    a += i
    
cnt = cnt + len(a)
print(cnt)
