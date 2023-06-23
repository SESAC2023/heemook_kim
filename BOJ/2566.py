# BOJ 2566번
max_val = -10e9

arr = [list(map(int, input().split())) for _ in range(9)]

행 = 1
for i in arr:
    열 = 1
    for j in i:
        if j > max_val:
            max_val = j
            coordinate = str(행) + ' ' + str(열)
        열 += 1
    행 += 1

print(max_val)
print(coordinate)
