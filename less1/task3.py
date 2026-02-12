import sympy as sym

f = sym.Function('f')
x = sym.Function('x')
y = sym.Function('y')
z = sym.Function('z')

t = sym.Symbol('t')

R =1
y = sym.cos(x(t))
print(sym.diff(y, x(t)))

y = sym.sin(x(t))
print(sym.diff(y, x(t)))

y = sym.tan(x(t))
print(sym.diff(y, x(t)))

y = sym.log(x(t))
print(sym.diff(y, x(t)))

y = sym.log(x(t))
print(sym.diff(y, x(t)))
y = sym.exp(x(t))
print(sym.diff(y, x(t)))

y = (x(t))**2
print(sym.diff(y, x(t)))

y = 3*x(t)**2 - 5 * sym.sin(4 * x(t))
print(sym.diff(y, x(t)))

y = t**2
print(sym.diff(y, t))