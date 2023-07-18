# BOJ 9506번
while True:
    n = int(input())
    if n == -1:
        break
    d = []
    for i in range(1, int(n**0.5)+1):
        if not n % i:
            d.extend([i, n//i])
    d.sort()
    d.remove(n)
    if sum(d) == n:
        sum_of_d = ' + '.join(map(str, d))
        print(f'{n} = {sum_of_d}')
    else:
        print(f'{n} is NOT perfect.')
