#örnek soru
from sympy import pprint
from sympy import Symbol, exp, sqrt, pi, Integral

x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
pprint(p)
pprint(Integral(p, (x, 11, 12)).doit().evalf())
