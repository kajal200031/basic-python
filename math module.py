>>> #math module
>>> #1st method
>>> import math
>>> print(math.sqrt(16))
4.0
>>> print(math.pi)
3.141592653589793
>>> #second method
>>> import math as m
>>> print(m.sqrt(16))
4.0
>>> print(m.pi)
3.141592653589793
>>> #third method
>>> from math import sqrt,pi
>>> print(sqrt(16))
4.0
>>> print(pi)
3.141592653589793
>>> #function of math module
>>> import math
>>> math.factorial(4)
24
>>> math.e
2.718281828459045
>>> #e is the euler's number
>>> math.radians(60)
1.0471975511965976
>>> math.floor(3)
3
>>> math.sin(60)
-0.3048106211022167
>>> math.cos(60)
-0.9524129804151563
>>> math.tan(60)
0.320040389379563
>>> math.log(10)(#base is e)
2.302585092994046
>>> math.log10(10)
1.0
>>> #base is 10
>>> math.pow(2,3)
8.0
>>> math.ceil(5.53466)
6
>>> math.floor(5.53466)
5
>>> math.exp(10)
22026.465794806718
>>> from math import pi
>>> r=3
>>> print("area of circle is:",pi*r**2)
area of circle is: 28.274333882308138
>>> from math import fsum
>>> a=[2,45,56.6,34,67]
>>> print("sum of the list is:",fsum(a))
sum of the list is: 204.6
>>> from math import pi
>>> r=3
>>> print("the circumference of the circle:",2*pi*r)
the circumference of the circle: 18.84955592153876
>>> #inf=infinity
>>> from math import inf
>>> float("inf")
inf
>>> type(inf)
<class 'float'>
>>> float("inf")==math.inf
True
>>> x=1e308
>>> math.inf>x
True
>>> math.inf<x
False
>>> math.inf + 1e308
inf
>>> math.inf /1e308
inf
>>> 
