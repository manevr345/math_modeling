import sympy as sym
from sympy.vector import CoordSys3D
N = CoordSys3D('N')
a = 4*N.i + 3*N.j
b = 4*N.i + -5*N.j
print(a+ b)
print(a - b)
print(a.dot(b))
print((a.magnitude()))

