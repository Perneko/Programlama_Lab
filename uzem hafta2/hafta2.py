from sympy import Symbol
x=Symbol('x')
y=Symbol('y')
p=x*(x+x)
print(p)
p=(x+2)*(x+3)
print(p)

from sympy import factor,expand
expr= x**2-y**2
print(factor(expr))#çarpanlarına ayırıyor

factors=factor(expr)
print(expand(factors))#çarpanlara ayrılmış denklemi tekrar tamlıyor

expr=x**3 + 3*x**2*y+3*x*y**2+y**3
factors = factor(expr)
print(factors)

from sympy import pprint
pprint(factors)#üstel bir şekilde çıktı veriyor

series = x
n=5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)

expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})#.subs() değerlere sayı vermeyi sağlıyor
print(res)
r=expr.subs({x:y-1})#x i yok ediyor x yerine y-1 yazıyor

series = x
n=5
x_value=10
for i in range(2,n+1):
    series = series + (x*i)/i
pprint(series)
series_value=series.subs({x:x_value})
print(series_value)





