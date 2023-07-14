# BOJ 10101번
angle = []
for i in range(3):
    angle.append(int(input()))

set_angle = set(angle)
if sum(angle) == 180 and len(set_angle) == 1:
    print('Equilateral')
elif sum(angle) == 180 and len(set_angle) == 2:
    print('Isosceles')
elif sum(angle) == 180:
    print('Scalene')
else:
    print('Error')
