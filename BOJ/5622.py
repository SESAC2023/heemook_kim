# BOJ 5622번
data = input()

dictionary = {
  'ABC':'2',
  'DEF':'3',
  'GHI':'4',
  'JKL':'5',
  'MNO':'6',
  'PQRS':'7',
  'TUV':'8',
  'WXYZ':'9'
}

str_num = ''
for i in data:
  for key, val in dictionary.items():
    if i in key:
      str_num += val

result = [int(j) + 1 if j != '1' else int(j) for j in str_num]

print(sum(result))
