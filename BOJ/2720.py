# BOJ 2720번
t = int(input())

money = [25, 10, 5, 1]

while t:
    c = int(input())
    
    answer = []
    for i in money:
        result = c // i
        c %= i
        answer.append(str(result))
    print(' '.join(answer))
    
    t -= 1
