# это пробная программа, которая не только, считает координату падения, но и строит график для наглядности
# числа взяты случайные
from numpy import *
from numpy.random import *
delta=1.0
x=linspace(-5,5,11)
y=-(x-1)**2+10+delta*(rand(11)-0.5)
x+=delta*(rand(11)-0.5)
x.tofile('x_data.txt', '\n')
y.tofile('y_data.txt', '\n')

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

# рисуем точки
plot(x,y,'+')
# рисуем кривую вида y = ax<sup>2</sup> + bx + c, подставляя из решения коэффициенты s[0], s[1], s[2]
plot(x_prec,s[0]*x_prec**2+s[1]*x_prec+s[2],'-',lw=2)

grid()

savefig('plot4.png')

# считаем координту падения
D = s[1]**2 - 4*s[0]*s[2]
otvet = (-1*s[1] - sqrt(D))/(2*s[0])
print(otvet)
