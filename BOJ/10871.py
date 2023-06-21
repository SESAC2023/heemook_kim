# BOJ 10871번
n, x = map(int, input().split())
arr = list(map(int, input().split()))

[print(i, end=' ') for i in arr if i < x]
