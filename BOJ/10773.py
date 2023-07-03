# BOJ 10773번
k = int(input())

stack = []
for _ in range(k):
    num = int(input())
    
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
        
print(sum(stack))
