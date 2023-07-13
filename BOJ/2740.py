# # BOJ 2740번
# 바로 출력
# n, m = map(int, input().split())

# matrix_a = [[] for _ in range(n)]

# for i in range(n):
#     x = list(map(int, input().split()))
#     matrix_a[i].extend(x)

# m, k = map(int, input().split())

# matrix_b = [[] for _ in range(m)]

# for j in range(m):
#     y = list(map(int, input().split()))
#     matrix_b[j].extend(y)

# for i in range(n):
#     for l in range(k):
#         result = 0
#         for j in range(m):
#             result += matrix_a[i][j] * matrix_b[j][l]
#         print(result, end=' ')
#     print()

# 행렬 다시 만든 후 출력
n, m = map(int, input().split())

matrix_a = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    matrix_a[i].extend(x)

m, k = map(int, input().split())

matrix_b = [[] for _ in range(m)]

for j in range(m):
    y = list(map(int, input().split()))
    matrix_b[j].extend(y)

result_matrix = [[0] * k for _ in range(n)]

for i in range(n):
    for l in range(k):
        for j in range(m):
            result_matrix[i][l] += matrix_a[i][j] * matrix_b[j][l]

for row in result_matrix:
    print(' '.join(map(str, row)))
