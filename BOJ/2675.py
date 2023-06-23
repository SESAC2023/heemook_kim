# BOJ 2675번
data = int(input())

problems = []
for i in range(data):
  problem = input().split(' ')
  problems.append(problem)

for i in problems:
  for j in i[1]:
    print(j * int(i[0]), end='')
  if j == i[1][-1]:
    print()
