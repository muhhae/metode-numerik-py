from rich import *
from rich.table import Table

def list():
    print("\nList\n")
    print("euler(f, x, y, h, xb):")
    print("heun(f, x, y, h, xb):")
    print("polygon(f, x, y, h, xb):")
    print("raltson(f, x, y, h, xb):")
    print("kutta(f, x, y, h, xb):")
    
def all(f, x, y, h, xb):
    euler(f, x, y, h, xb)
    heun(f, x, y, h, xb)
    polygon(f, x, y, h, xb)
    raltson(f, x, y, h, xb)
    kutta(f, x, y, h, xb)
    
def hitung(f, x, y, h, xb, ft):
    table = Table(title="Hasil Perhitungan")
    
    table.add_column("x", justify="left", style="blue")
    table.add_column("F(x)", justify="left", style="yellow")
    
    while x <= xb:
        table.add_row(str(x), str(y))
        y = ft(f, x, y, h)
        x += h
    table.add_row(str(x), str(y))
    y = ft(f, x, y, h)
    x += h
    print(table)

def euler(f, x, y, h, xb):
    print("\nEuler\n")
    ft = lambda f, x, y, h: y + f(x) * h
    hitung(f, x, y, h, xb, ft)

def heun(f, x, y, h, xb):
    print("\nHeun\n")
    ft = lambda f, x, y, h: y + h*(f(x)+ f(x+h))/2
    hitung(f, x, y, h, xb, ft)
    
def polygon(f, x, y, h, xb):
    print("\nPolygon\n")
    ft = lambda f, x, y, h: y + h*f(x +h/2)
    hitung(f, x, y, h, xb, ft)
    
def raltson(f, x, y, h, xb):
    print("\nRaltson\n")
    ft = lambda f, x, y, h: y + h*(f(x)+2*f(x+0.75*h))/3
    hitung(f, x, y, h, xb, ft)
    
def kutta(f, x, y, h, xb):
    print("\nKutta\n")
    ft = lambda f, x, y, h: y +  h*(f(x )+4*f(x+h/2)+f(x+h))/6
    hitung(f, x, y, h, xb, ft)