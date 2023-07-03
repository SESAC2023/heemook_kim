# BOJ 4949번
while True:
    sentence = input().rstrip()
    stack = []

    if sentence == '.':
        break

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)

    if stack:
        print('no')
    else:
        print('yes')
