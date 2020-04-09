import sympy as sym
from sympy import Symbol
from sympy import pprint

%matplotlib notebook
import sympy.plotting as syp
sigma = Symbol('sigma')
x= Symbol('x')
mu= Symbol('mu')
pprint(2*sym.pi*sigma)

part1=1/(sym.sqrt(2*sym.pi*sigma**2))
part2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))

my_gaus_f=part1*part2
pprint(my_gaus_f)

print(syp.plot(my_gaus_f.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distribution'))#grafik çizdi
x_values=[]
y_values=[]
for value in range(-100,100):
    #y=my_gaus_f.subs({mu:10,sigma:30,x:value})
    y=my_gaus_f.subs({mu:10,sigma:30,x:value}).evalf()
    #y=my_gaus_f.subs({mu:10,sigma:30,x:value}).doit()
    y_values.append(y)
    x_values.append(value)
    print(x,y)
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()



