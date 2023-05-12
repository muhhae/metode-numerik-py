from math import *

print("\n~~FungsiMetnum Function List~~\n")
print("bagidua(xa, xb, f, error, imax) \n\t- metode bagi dua \n")
print("regulafalsi(xa,xb, f, error, imax) \n\t- metode regula falsi \n")
print("newtonraphson(xr, f, ft, error, imax) \n\t- metode newton raphson \n")
print("secant(xa, xb, f, error, imax) \n\t- metode secant \n")
print("fungsi(xa,xb,xr, f,ft, error, imax) \n\t- semua metode \n")


def bagidua(xa, xb, f, error, imax):
    print("Metode Bagi dua\n")
    i = 1
    xc = 0
    while True:
        xc = (xa+xb)/2
        print(i, 'x = ', xc, 'f(x) = ', f(xc))
        if abs(f(xc))<error or i >= imax:
            print('Akar :',xc)
            break
        else:
            if f(xc)*f(xa) > 0:
                xa = xc
            else:
                xb = xc
        i+=1

def regulafalsi(xa,xb, f, error, imax):
    print('metode regula falsi\n')
    i = 1
    while True:
        xc = xb-f(xb)*(xb-xa)/(f(xb)-f(xa))
        print(i, 'x = ', xc, 'f(x) = ', f(xc))
        if abs(f(xc)) < error or i >= imax:
            print('Akar :',xc)
            break
        else:
            if f(xc)*f(xa) > 0:
                xa = xc
            else:
                xb = xc
    i += 1

def newtonraphson(xr, f, ft, error, imax):
    print("Metode Newton Raphson\n")
    i = 1
    while True:
        print(i, 'x = ', xr, 'f(x) = ', f(xr))
        if (abs(f(xr)) < error) or i >= imax:
            print('akar = ', xr)
            break
        else:
            xr = xr - f(xr)/ft(xr)
    i+=1

def secant(xa, xb, f, error, imax):
    print("Metode secant\n")
    xc = 0
    i = 1
    while True:
        xc = xb - f(xb)/((f(xa)-f(xb))/(xa-xb))
        print(i, 'x = ', xc, 'f(x) = ', f(xc))
        if (abs(f(xc))<error or i >= 10):
            print("akar = ", xc)
            break
        else:
            xa, xb = xc, xa
            i += 1
    
def fungsi(xa,xb,xr, f,ft, error, imax):
    bagidua(xa, xb, f, error, imax)
    print('\n')
    regulafalsi(xa, xb, f, error, imax)
    print('\n')
    newtonraphson(xr, f, ft, error, imax)
    print('\n')
    secant(xa, xb, f, error, imax)
    
    


