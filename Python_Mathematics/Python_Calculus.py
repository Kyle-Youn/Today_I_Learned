from sympy import Symbol, diff, integrate

x = Symbol('x')

f = x**2 + 2*x + 1

print(diff(f, x))  # 미분

print(integrate(f, x))  # 적분
