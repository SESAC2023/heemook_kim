# BOJ 25206번
학점 = []
등급 = []

dic = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

for _ in range(20):
    과목별 = input().split()
    if 과목별[-1] != 'P':
        학점.append(float(과목별[1]))
        등급.append(dic[과목별[-1]])

평점 = [i*j for i,j in zip(학점, 등급)]
answer = sum(평점) / sum(학점)
print(answer)
