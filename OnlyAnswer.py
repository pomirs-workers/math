from numpy import *
from pylab import *
from scipy.linalg import *

# читаем данные из файлов
x=fromfile('x_data.txt',float,sep='\n')
y=fromfile('y_data.txt',float,sep='\n')

# задаем вектор m = [x**2, x, E]
m=vstack((x**2,x,ones(11))).T
# находим коэффициенты при составляющих вектора m
s=lstsq(m,y)[0]
x_prec=linspace(-5,20,101)

D = s[1]**2 - 4*s[0]*s[2]
otvet = (-1*s[1] - sqrt(D))/(2*s[0])
print(otvet)
