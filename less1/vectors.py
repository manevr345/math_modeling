import sympy as sym
from sympy.vector import CoordSys3D
N = CoordSys3D('N')
a, b, c = sym.symbols('a b c')

v = N.i - 2*N.j
print(v/3)
v1 = 2*N.i + 3*N.j - N.k
print(v1*2)
sol = v1.dot(v)
print(sol)
print(v1+v)
print(v-v1)