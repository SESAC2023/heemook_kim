# BOJ 1269번
a, b = map(int, input().split())

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

a_only = a_set - b_set
b_only = b_set - a_set

print(len(a_only) + len(b_only))
