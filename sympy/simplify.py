from sympy import *

x, y, z = symbols('x y z')

y = simplify(sin(x)**2 + cos(x)**2)
print(y)
'''
1
'''

y = simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
print(y)
'''
x-1
'''


y = simplify((x**3 + x**2 - x - 1)*(x**2 + 2*x + 1)*(x**2-(2*x**2-x**2))/(x**2 + 2*x + 1))
print(y)
'''
0
'''
