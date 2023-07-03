# BOJ 2231번
N = int(input())

M_list = []

for M in range(1, N):
  if len(str(M)) == 1:
    if N == 2*M:
      M_list.append(M)
    else:
      pass

  else:
    n_list = [M]
    for i in range(0, len(str(M))):
      n_list.append(int(str(M)[i]))
    if sum(n_list) == N:
      M_list.append(M)
    else:
      pass

if len(M_list) == 0:
  print(0)
else:
  print(min(M_list))
