# BOJ 1181번
N = int(input())

words = []
while N > 0:
    word = input()
    words.append(word)        
    N -= 1

words = list(set(words))
words = sorted(words)
words.sort(key=lambda x : len(x))

for i in words:
    print(i)
