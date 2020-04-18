import sympy as sym
from sympy import Symbol
from sympy import pprint

p=Symbol('p')
x=Symbol('x')
n=Symbol('n')

my_f_3_part_0=sym.factorial(n)/sym.factorial(x)*sym.factorial(n-x)

pprint(my_f_3_part_0)

my_f_3_part_1=p**x

pprint(my_f_3_part_1)

my_f_3_part_2= (1-p)**(n-x)

pprint(my_f_3_part_2)

my_f_3=my_f_3_part_0 * my_f_3_part_1 * my_f_3_part_2
pprint(my_f_3)

sym.plot(my_f_3.sub({p:0.5,n:50}),(x,0,50),title='binomin distribution for n= 50')
