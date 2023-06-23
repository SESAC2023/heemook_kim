# BOJ 10809번
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = input()

for i in alphabet:
    if i in word:
        idx = word.index(i)
    else:
        idx = -1    
    print(idx, end=' ')
