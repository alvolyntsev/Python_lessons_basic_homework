import math
print('ax^2+bx+c=0')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
x1=(-b+math.sqrt(b*b-4*a*c))/2*a
x2=(-b-math.sqrt(b*b-4*a*c))/2*a
print('x1=', x1)
print('x2=', x2)