# BOJ 1966번
n = int(input())

for _ in range(n):
    length, target = map(int, input().split())
    queue = [i for i in range(length)]

    weights = list(map(int, input().split()))
    comparison = sorted(weights, reverse=True)

    result = []
    for i in comparison:
        while queue:
            if i == weights[0]:
                x = queue.pop(0)
                y = weights.pop(0)
                result.append(x)
                break        
            else:
                x = queue.pop(0)
                y = weights.pop(0)
                queue.append(x)
                weights.append(y)
            
    print(result.index(target) + 1)
