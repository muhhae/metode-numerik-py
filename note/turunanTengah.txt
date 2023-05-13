Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
f = x:x**3
SyntaxError: invalid syntax
f =lambda x:x**3
f(2)
8
>>> f(1,1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f(1,1)
TypeError: <lambda>() takes 1 positional argument but 2 were given
>>> f(1.1)
1.3310000000000004
>>> ft = lambda f,x,h:(f(x+h)-f(x-h))/(2*h)
>>> ft(f, 1, 1)
4.0
>>> ft(f, 1, 0.25)
3.0625
>>> ft(f, 1, 0.1)
3.0100000000000016
>>> ft(f, 1, 0.00001)
3.000000000097369
>>> g = lambda x:x**2+3*x-4
>>> ft(g, 1, 0.1)
5.000000000000002
>>> ftt = lambda f,x,h: (f(x+h) - 2*f(x)+ f(x-h))/h**2
>>> ftt(f, 1, 0,1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ftt(f, 1, 0,1)
TypeError: <lambda>() takes 3 positional arguments but 4 were given
>>> ftt(f, 1, 0.1)
6.000000000000049
>>> ft3 = lambda f, x, h: (f(x+2h) - 2*f(x+h)+2*f(x-h) - f(x-2h))/(2*h**3)
SyntaxError: invalid decimal literal
>>> ft3 = lambda f, x, h: (f(x+2*h) - 2*f(x+h)+2*f(x-h) - f(x-2*h))/(2*h**3)
>>> ft3(f, 1, 0,1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ft3(f, 1, 0,1)
TypeError: <lambda>() takes 3 positional arguments but 4 were given
>>> ft3(f, 1, 0.1)
5.999999999999504
>>> ft3(f, 2, 0.1)
5.999999999999337
>>> ft3(f, 4, 0.1)
6.000000000025095
>>> ft4 = lambda f, x, h: (f(x-2*h) - 4*f(x-h) + 6 * f(x) -4 * f(x+h) + f(x+2*h))/h**4
>>> ft4(f, 1, 0.1)
-2.2204460492503128e-11
>>> ft4(f, 2, 0.1)
3.5527136788005e-11
