import sympy as sym
# Определяем функции
f = sym.Function('f')
x=sym.Function('x')
t = sym.Symbol('t')
f = sym.tan(x(t))
dir = sym.dif(f, x(t))
