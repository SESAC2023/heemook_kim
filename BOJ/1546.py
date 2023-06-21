# BOJ 1546번
m = int(input())

score = list(map(int, input().split()))
h = max(score)
re_score = list(map(lambda x: x/h*100, score))

print(sum(re_score)/m)
