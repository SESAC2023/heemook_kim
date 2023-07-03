# BOJ 9935번
sentence = input()
bomb = input()

stack = []

for i in sentence:
    stack.append(i)
    cond = len(stack) - len(bomb)
    while cond >= 0:
        if ''.join(stack[cond:]) == bomb:
            for _ in bomb:
                stack.pop()
        else:
            break
if stack:
    print(''.join(stack))
else:
    print('FRULA')
