# BOJ 11478번
s = input()

result = []
for i in range(1, len(s) + 1): # 문자열 길이 지정 (1, 2, 3, ...)
    for j in range(len(s)): # 문자열 시작 문자 지정
        if len(s[j : j + i]) == i: # ex) len == 3 -> bc 경우처럼 불필요한 for 문 방지
            result.append(s[j : j + i])
        else:
            break

answer = set(result)

print(len(answer))
