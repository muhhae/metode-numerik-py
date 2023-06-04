from math import *

def list():
    print("Trapesium(f, a, b, n=1, out = True)")
    print("TitikTengah(f, a, b, n=1, out = True)")
    print("INC2(f, a, b, n=1, out = True)")
    print("INC3(f, a, b, n=1, out = True)")
    print("INC4(f, a, b, n=1, out = True)")

def all(f, a, b, n = 4, out = True):
    Trapesium(f, a, b, n, out)
    TitikTengah(f, a, b, n, out)
    INC2(f, a, b, n, out)
    INC3(f, a, b, n, out)
    INC4(f, a, b, n, out)
    for i in range(2, 6):
        GaussKuadratur(f, a, b, i, out)

def Trapesium(f, a, b, n=1, out = True):
    print("\nMetode Trapesium")
    I = lambda a, b: abs((b - a) / 2 * (f(b) + f(a)))
    xa = a; h = (b-a) / n;luas = 0
    while xa < b :
        xb = xa + h
        luas += abs(I(xa, xb))
        if out:
            print("(", xa, ",", xb, ") = ", I(xa, xb),sep="")
            print("I = ", luas, "\n")
        xa = xb
    print("I =", luas)
    return luas

def TitikTengah(f, a, b, n=1, out = True):
    print("\nMetode Titik Tengah")
    I = lambda a, b: abs((b - a) * f((a + b) / 2))
    xa = a; h = (b-a) / n;luas = 0
    while xa < b :
        xb = xa + h
        luas += abs(I(xa, xb))
        if out:
            print("(", xa, ",", xb, ") = ", I(xa, xb),sep="")
            print("I = ", luas, "\n")
        xa = xb
    print("I =", luas)
    return luas

def INC2(f, a, b, n=1, out = True):
    print("\nNewton-Cotes Simpson 1/3")
    h = (b-a) / n
    d = h / 2
    I = lambda a: 1 / 3 * d * (f(a) + 4 * f(a + d) + f(a + h))
    luas = 0
    for i in range(n):
        luas += abs(I(a))    
        if out:
            print("(", a, ",", a + h, ") = ", I(a),sep="")
            print("I = ", luas, "\n")
        a = a + h
    print("I =", luas)
    return luas

def INC3(f, a, b, n=1, out = True):
    print("\nNewton-Cotes Simpson 3/8")
    h = (b - a) / n
    d = h/3
    I = lambda a: 3 / 8 * d * (f(a) + 3 * f(a + d) + 3 * f(a + 2 * d) + f(a + h))
    luas = 0
    for i in range(n):
        luas += abs(I(a))
        if out:
            print("(", a, ",", a + h, ") = ", I(a),sep="")
            print("I = ", luas, "\n")
        a = a + h
    print("I =", luas)
    return luas

def INC4(f, a, b, n=1, out = True):
    print("\nNewton-Cotes Boole 2/45")
    h = (b - a) / n
    d = h/4
    I = lambda a: 2 / 45 * d * ( 7 * f(a) + 32 * f(a + d) + 12 * f(a + 2 * d) + 32 * f(a + 3 * d) + 7 * f(a + h))
    luas = 0
    for i in range(n):
        luas += abs(I(a))
        if out:
            print("(", a, ",", a + h, ") = ", I(a),sep="")
            print("I = ", luas, "\n")
        a = a + h
    print("I =", luas)
    return luas

# def NewtonCotes(f, a, b, n, o, out = True):    
    

def GaussKuadratur(FungsiAwal, a, b, n=2, out = True):
    print("\nMetode Gauss Kuadratur Orde", n)
    
    if abs(b-a)<1e-10: return 0
    
    c = [
            [1, 1],
            [0.5555555555555556, 0.8888888888888888, 0.5555555555555556],
            [0.3478548451374538, 0.6521451548625461, 0.6521451548625461, 0.3478548451374538],
            [0.2369268850561891, 0.4786286704993665, 0.5688888888888889, 0.4786286704993665, 0.2369268850561891]
        ]
    x = [
            [-0.5773502691896257, 0.5773502691896257],
            [-0.7745966692414834, 0, 0.7745966692414834],
            [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526],
            [-0.9061798459386640, -0.5384693101056831, 0 ,0.5384693101056831, 0.9061798459386640]
        ]
    
    def f(t):
        x=((a+b) + (b-a)*t)/2
        return FungsiAwal(x)
    
    total = 0
    n -= 2
    for i in range(n + 2):
        if out :
            print("f(", x[n][i], ") * ", c[n][i], " = ", f(x[n][i]) * c[n][i],'\n', sep="")
        total += f(x[n][i]) * c[n][i]
    
    print("I =", total * (b-a) / 2)
    return total * (b-a) / 2