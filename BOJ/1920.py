# BOJ 1920번 이분 탐색으로 풀기
N = int(input())
A = sorted(list(map(int, input().split(' '))))[:N]

M = int(input())
X = list(map(int, input().split(' ')))[:M]

def 이분탐색(lst, num):
    start, end = 0, len(lst)-1
    
    while start <= end:
        mid = (start + end) // 2
        if num == lst[mid]:
            return 1
        elif num > lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for x in X:
    print(이분탐색(A, x))
