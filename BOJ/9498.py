score = int(input())

if (score >= 90) & (score <= 100):
  print('A')
elif (score >= 80) & (score < 90):
  print('B')
elif (score >= 70) & (score < 80):
  print('C')
elif (score >= 60) & (score < 70):
  print('D')
else:
  print('F')
