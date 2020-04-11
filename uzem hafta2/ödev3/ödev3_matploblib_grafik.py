import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp
x=Symbol('x')#sembol atamaları
lamda=Symbol('lambda')

p=1-sym.exp(-lamda*x)#Exponential Distribution türkçe adıyla üstel dağılım fonksiyonu
pprint(p)#Sabit ortalama değişme haddinde ortaya çıkan bağımsız olaylar arasındaki zaman aralığını modelleştirirken bir üstel dağılım doğal olarak ortaya çıkar.

x_value=[]
y_value=[]
for value in range(6):#n=5+1
    y=p.subs({lamda:1,x:value}).evalf()
    y_value.append(y)#karşılık gelen değerleri listeye atanıyor
    x_value.append(value)
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(x_value,y_value)
plt.show()#matplotlib yöntemiyle çıktı veren grafik
