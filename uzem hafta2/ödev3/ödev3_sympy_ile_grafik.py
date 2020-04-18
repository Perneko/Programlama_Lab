import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp
x=Symbol('x')#sembol atamaları
lamda=Symbol('lambda')

p=1-sym.exp(-lamda*x)#Exponential Distribution türkçe adıyla üstel dağılım fonksiyonu
pprint(p)#Sabit ortalama değişme haddinde ortaya çıkan bağımsız olaylar arasındaki zaman aralığını modelleştirirken bir üstel dağılım doğal olarak ortaya çıkar.

print(syp.plot(p.subs({lamda:1}),(x,0,5),title='Exponential Distribution'))#sympy sayesinde çizilen grafik
