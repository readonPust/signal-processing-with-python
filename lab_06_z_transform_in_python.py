from sympy import *

x = [1, 2, 3, 4, 5]
length = len(x)
y = 0
z = symbols('z')
for i in range(length):
    y = y + x[i] * z ** (-i)
print(y)