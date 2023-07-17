# BOJ 5086번
while True:
    x, y = map(int, input().split())

    if not x and not y:
        break
    elif y // x and not y % x:
        print('factor')
    elif x // y and not x % y:
        print('multiple')
    else:
        print('neither')
