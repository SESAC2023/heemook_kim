# BOJ 9012번
T = int(input())

eraser = '()'
for _ in range(T):
    x = input()

    while x:
        if eraser in x:
            x = x.replace(eraser, '')
        else:
            break
        
    if len(x) > 0:
        print('NO')
    else:
        print('YES')
        
    
