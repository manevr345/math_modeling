import sympy as sym
# Определяем функции
f = sym.Function('f')
x=sym.Function('x')
y=sym.Function('y')
z=sym.Function('z')
# Определяем пременные
t = sym.Symbol('t')
R = 1
f = x(t) + y(t)**2 + z(t)**2 - R**2
print(sym.diff(f, x(t)))
print(sym.diff(f, z(t)))
print(sym.diff(sym.diff(f, t)))