# BOJ 2869번
a, b, v = map(int, input().split())

if (v - a) % (a - b):
    day = (v - a) // (a - b) + 1
else:
    day = (v - a) // (a - b)

print(day + 1) # 0일부터가 아니라 1일부터 세기 때문에
