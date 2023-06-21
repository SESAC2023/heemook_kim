# BOJ 10811번
n, m = map(int, input().split(' '))

basket = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split(' '))
    reverse = basket[i-1:j]
    basket[i-1:j] = reverse[::-1]
    
for _ in basket:
    print(_, end=' ')
