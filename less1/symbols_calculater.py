import math
import sympy as sym
print(math.sqrt(3))
print(sym.sqrt(3))
print(sym.sqrt(3)*2)
x, y = sym.symbols('x y')
expr = x + 2*y
print(type(expr))
print(expr +1 + x)
print(x*expr)
print(sym.sin(x**2)- sym.exp(-2*x) + sym.cos(sym.pi / x))