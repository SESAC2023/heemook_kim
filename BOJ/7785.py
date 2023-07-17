# BOJ 7785번
import sys
input = sys.stdin.readline
n = int(input().rstrip())

dic = dict()
for i in range(n):
    name, log = input().split()
    if log == 'enter':
        dic.update({name : log})
    if log == 'leave':
        dic.pop(name)

for key in sorted(dic.keys(), reverse=True): # dictionary 는 sort 가 없고, sorted 만 있다 !
    print(key)
