# BOJ 10816번
from collections import Counter

N = input()
n_cards = input().split()
M = input()
m_cards = input().split()

counter = Counter(n_cards)

for card in m_cards:
    print(counter[card], end=' ')
