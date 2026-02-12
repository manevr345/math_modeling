import sympy as sym
x = sym.symbols('x')
expr = sym.sin(x) + sym.log(x, 10) - x
solve_expr = sym.solveset(expr, x)
print(solve_expr)
expr = 2**x - sym.log(x, 10) - sym.cos(x)**-1
solve_expr = sym.solveset(expr, x)
print(solve_expr)