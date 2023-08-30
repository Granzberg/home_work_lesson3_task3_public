import cmath

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
x1 = - b - (cmath.phase((b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
x2 = - b + (cmath.phase((b ** 2 - 4 * a * c) ** 0.5) / 2 * a)

print('x1 = ',  x1, "\nx2 = ", x2)
