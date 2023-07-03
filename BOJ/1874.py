# BOJ 1874번
n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

comparison = []
stack = []
result =''
idx = 0

for j in range(1, n + 1):
    comparison.append(j)
    result += '+'

    while comparison:
        if comparison[-1] == arr[idx]:
            wanted = comparison.pop()
            stack.append(wanted)
            result += '-'
            idx += 1
        else:
            break

if comparison:
    print('NO')
else:    
    print('\n'.join(result))
