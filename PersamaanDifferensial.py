from rich import *

def pdb(f,x,y,h,xb,tipe):
    if tipe=="euler" :
        fa=lambda ft,xi,yi,h: yi + ft(xi)* h
    elif tipe=="heun"  :
        fa=lambda f,xi,yi,h:yi + h*(f(xi)+ f(xi+h))/2
    elif tipe=="polygon":
        fa =lambda f,xi,yi,h:yi + h*f(xi +h/2)
    elif tipe=="raltson":
        fa=lambda f,xi,yi,h:yi + h*(f(xi)+2*f(xi+0.75*h))/3                   
    elif tipe=="kutta" :
        fa=lambda f,xi,yi,h:yi +  h*(f(xi )+4*f(xi+h/2)+f(xi+h))/6
        
    while x<=xb:
        print(x,y)
        y=fa(f,x,y,h)
        x+=h