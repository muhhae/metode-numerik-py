Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
KeyboardInterrupt
f=lambda x:2*x*x-3
for x in range(10) :print (x,f(x))

0 -3
1 -1
2 5
3 15
4 29
5 47
6 69
7 95
8 125
9 159
for x in range(-3,3) : print (x,f(x))

-3 15
-2 5
-1 -1
0 -3
1 -1
2 5
for x in range(20) :print(x/10-1.3, f(x/10-1.3))

-1.3 0.38000000000000034
-1.2 -0.1200000000000001
-1.1 -0.5799999999999996
-1.0 -1.0
-0.9 -1.38
-0.8 -1.7199999999999998
-0.7000000000000001 -2.0199999999999996
-0.6000000000000001 -2.28
-0.5 -2.5
-0.4 -2.6799999999999997
-0.30000000000000004 -2.82
-0.19999999999999996 -2.92
-0.10000000000000009 -2.98
0.0 -3.0
0.09999999999999987 -2.98
0.19999999999999996 -2.92
0.30000000000000004 -2.82
0.3999999999999999 -2.68
0.5 -2.5
0.5999999999999999 -2.2800000000000002
for x in range(20) :print(x/40-1.3,f(x/40-1.3))

-1.3 0.38000000000000034
-1.2750000000000001 0.25125000000000064
-1.25 0.125
-1.225 0.0012500000000006395
-1.2 -0.1200000000000001
-1.175 -0.23874999999999957
-1.1500000000000001 -0.35499999999999954
-1.125 -0.46875
-1.1 -0.5799999999999996
-1.075 -0.6887500000000002
-1.05 -0.7949999999999999
-1.025 -0.8987500000000002
-1.0 -1.0
-0.9750000000000001 -1.0987499999999997
-0.9500000000000001 -1.1949999999999998
-0.925 -1.2887499999999998
-0.9 -1.38
-0.875 -1.46875
-0.8500000000000001 -1.5549999999999997
-0.8250000000000001 -1.6387499999999997
for x in range(10) :print(x/40-1.225,f(x/40-1.225))

-1.225 0.0012500000000006395
-1.2000000000000002 -0.11999999999999922
-1.175 -0.23874999999999957
-1.1500000000000001 -0.35499999999999954
-1.125 -0.46875
-1.1 -0.5799999999999996
-1.0750000000000002 -0.6887499999999993
-1.05 -0.7949999999999999
-1.0250000000000001 -0.8987499999999993
-1.0 -1.0
for x in range(10) :print(x/100-1.225,f(x/100-1.225))

-1.225 0.0012500000000006395
-1.215 -0.04754999999999976
-1.205 -0.09594999999999976
-1.195 -0.1439499999999998
-1.185 -0.1915499999999999
-1.175 -0.23874999999999957
-1.165 -0.28554999999999975
-1.155 -0.33194999999999997
-1.145 -0.3779499999999998
-1.135 -0.4235500000000001
KeyboardInterrupt
f = lambda x:4*x**3-6*x*x+7*x-2.3
xa,xb = 0,1
while True
SyntaxError: incomplete input
while True:
    xc = (xa+xb)/2
    if abs(f(xc)):
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 0.5
f(0.5)
0.20000000000000018
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.1:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 0.4375
f(0.4375)
-0.05097656249999982
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.0001:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 0.45013427734375
f(0.45013427734375)
4.112688675395049e-05
jumlah_akar = 0
for x in range (-100,100,10):print(x,f(x))

-100 -4060702.3
-90 -2965232.3
-80 -2086962.3
-70 -1401892.3
-60 -886022.3
-50 -515352.3
-40 -265882.3
-30 -113612.3
-20 -34542.3
-10 -4672.3
0 -2.3
10 3467.7
20 29737.7
30 102807.7
40 246677.7
50 485347.7
60 842817.7
70 1343087.7
80 2010157.7
90 2868027.7
for x in range (10):print(x/10,f(x))

0.0 -2.3
0.1 2.7
0.2 19.7
0.3 72.7
0.4 185.7
0.5 382.7
0.6 687.7
0.7 1124.7
0.8 1717.7
0.9 2490.7
for x in range (10):print(x/10,f(x/10))

0.0 -2.3
0.1 -1.6559999999999997
0.2 -1.1079999999999997
0.3 -0.6319999999999997
0.4 -0.20399999999999974
0.5 0.20000000000000018
0.6 0.6040000000000005
0.7 1.032
0.8 1.5080000000000005
0.9 2.056
f = lambda x:x*x/2 - 2*x-2
for x in range(10):print(x, f(x))

0 -2.0
1 -3.5
2 -4.0
3 -3.5
4 -2.0
5 0.5
6 4.0
7 8.5
8 14.0
9 20.5
for x in range(-100,100,10):print(x, f(x))

-100 5198.0
-90 4228.0
-80 3358.0
-70 2588.0
-60 1918.0
-50 1348.0
-40 878.0
-30 508.0
-20 238.0
-10 68.0
0 -2.0
10 28.0
20 158.0
30 388.0
40 718.0
50 1148.0
60 1678.0
70 2308.0
80 3038.0
90 3868.0
xa,xb = -10,0
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.0001:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : -0.828399658203125
xa,xb = 0,10
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.0001:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 4.8284149169921875
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.1:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 4.8284149169921875
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.1:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 4.8284149169921875
xa,xb = 0,10
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.1:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 4.84375
xa,xb = -10,0
while True:
    xc = (xa+xb)/2
    if abs(f(xc))<0.1:
        print('Akar :',xc)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : -0.859375
xa,xb = 0,10
i = 0
while True:
    i += 1
    xc = (xa+xb)/2
    if abs(f(xc))<0.1:
        print('Akar :',xc,'dalam : %d iterasi. '%i)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 4.84375 dalam : 6 iterasi. 
xa,xb = 0,10
i = 0
while True:
    i += 1
    xc = xb-f(xb)*(xb-xa)/(f(xb)-f(xa))
    if abs(f(xc))<0.1:
        print('Akar :',xc,'dalam : %d iterasi. '%i)
        break
    else:
        if f(xc)*f(xa) > 0:
            xa = xc
        else:
            xb = xc

            
Akar : 4.8081438041302444 dalam : 10 iterasi. 
>>> ft = lambda x:x-2
>>> xa,xb,i=0,10,0
>>> while True:
...     i += 1
...     xc = xb-f(xb)/ft(xb)
...     if abs(f(xc))<0.1:
...         print('Akar :',xc,'dalam : %d iterasi. '%i)
...         break
...     xb = xc
... 
...     
Akar : 4.843780727630285 dalam : 3 iterasi. 
>>> while True:
...     i += 1
...     xc = xb-f(xb)/ft(xb)
...     if abs(f(xc))<0.1:
...         print('Akar :',xc,'dalam : %d iterasi. '%i)
...         break
...     xb = xc
... 
...     
Akar : 4.843780727630285 dalam : 4 iterasi. 
>>> i = 5
>>> while True:
...     i += 1
...     xc = xb-f(xb)/ft(xb)
...     if abs(f(xc))<0.1:
...         print('Akar :',xc,'dalam : %d iterasi. '%i)
...         break
...     xb = xc
... 
...     
Akar : 4.843780727630285 dalam : 6 iterasi. 
>>> KeyboardInterrupt
>>> xb,i = 10,0
>>> 
>>> while True:
...     i += 1
...     xc = xb-f(xb)/ft(xb)
...     if abs(f(xc))<0.1:
...         print('Akar :',xc,'dalam : %d iterasi. '%i)
...         break
...     xb = xc
... 
...     
Akar : 4.843780727630285 dalam : 3 iterasi. 
