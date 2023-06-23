# BOJ 10798
result = []
for _ in range(5):
    sentence = input()
    sentence = sentence.ljust(15)
    result.append(sentence)

answer = ''
for _ in range(15):
    answer += result[0][_] + result[1][_] + result[2][_] + result[3][_] + result[4][_]
    
print(answer.replace(' ', ''))
