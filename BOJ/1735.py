# BOJ 1735번
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a = a1 * b2 + a2 * b1
b = b1 * b2

from math import gcd
x = gcd(a, b)

print(int(a/x), int(b/x))
