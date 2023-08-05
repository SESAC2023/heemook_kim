# BOJ 2346번
"""
rotate 방향
    deque.rotate(-1) : 음수인 경우, 앞의 요소가 뒤로
        => deque([1, 2, 3, 4, 5]) -> deque([2, 3, 4, 5, 1])
    deque.rotate(1) : 양수인 경우, 뒤의 요소가 앞으로
        => deque([1, 2, 3, 4, 5]) -> deque([5, 1, 2, 3, 4])
"""
from collections import deque

n = int(input())

balloon = deque(i for i in range(1, n + 1))
cmd = deque(map(int, input().split()))

while balloon:
    num = balloon.popleft()
    next = cmd.popleft()
    if next > 0: # 시계방향으로 rotate 해야 하는 경우
        next -= 1 # 이미 다음 요소부터 시작이므로 -1 (pop 을 한 순간 자동으로 다음 요소가 시작점이 되므로)
    print(num, end=' ')
    balloon.rotate(-next) # next % len() 만큼만 rotate 하는 것이 더 효율적일 듯
    cmd.rotate(-next)
