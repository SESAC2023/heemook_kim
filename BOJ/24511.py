# BOJ 24511번
import sys
input = sys.stdin.readline

# 자료구조 개수
n = int(input().rstrip())

# 수열 a: 자료구조 정보
a = list(map(int, input().split())) # queue => 0, stack => 1

# 수열 b: i번 자료구조에 들어 있는 원소(각각 1개씩 들어 있음)
b = list(map(int, input().split()))

# 삽입할 수열 길이
m = int(input().rstrip())

# 삽입할 수열 c
c = list(map(int, input().split()))

"""
# (1)번 방법
# 실제로 넣었다 빼는 과정 구현 -> 시간초과
from collections import deque
b = [deque(_) for _ in b]

result = []
for i in c:
    for j in range(n):
        b[j].append(i)
        if a[j]: # stack
            i = b[j].pop()
        else: # queue
            i = b[j].popleft()
    result.append(i)
print(*result)

"""
"""
# (2)번 방법
# stack -> stack은 넣은 원소 그대로 다시 나오므로 pass
# queue -> queue는 넣은 원소랑 나오는 원소가 서로 바뀜
# => 시간 초과
for i in c:
    for j in range(n):        
        if a[j]: # stack
            pass
        else: # queue
            i, b[j] = b[j], i
    print(i, end=' ')

"""
# (3)번 방법
# 처음부터 stack은 빼 버리기
# queue는 자료구조의 원소를 밀어내므로
# => 결국, 마지막 원소가 출력됨
from collections import deque
result = deque()
for i, j in zip(a, b): # 자료구조와 원소 묶기
    if not i: # queue일 때만
        result.append(j)

answer = []
for i in c:
    result.appendleft(i) # 삽입하면 원래 queue의 원소를 다음 queue로 밀어냄(현재 queue 개수가 삽입할 수열 길이보다 작을 수도 있으므로 꼭 필요)
    answer.append(result.pop()) # 결국 맨 마지막 원소 출력
print(*answer)
