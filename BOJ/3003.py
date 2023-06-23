# BOJ 3003번
chess = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))

for i in range(6):
    result = chess[i] - n[i]
    print(result, end=' ')
