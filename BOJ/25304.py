# BOJ 25304번
total = int(input())
kind = int(input())

for _ in range(kind):
    price, count = map(int, input().split())
    total -= price * count
    
if total == 0:
    print('Yes')
else:
    print('No')
