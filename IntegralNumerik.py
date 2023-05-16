def list():
    print("Trapesium(f, a, b, n=1):")
    print("Titiktengah(f, a, b, n=1):")
    print("INC2(f, a, b, n=1):")

def Trapesium(f, a, b, n=1):
    itrapesium = lambda f, a, b: abs((b - a) / 2 * (f(b) + f(a)))
    xa = a; h = (b-a) / n;luas = 0
    while xa < b :
        xb = xa + h
        luas += itrapesium(f, xa, xb)
        xa = xb
    return luas

def TitikTengah(f, a, b, n=1):
    ititiktengah = lambda f, a, b: abs((b - a) * f((a + b) / 2))
    xa = a; h = (b-a) / n;luas = 0
    while xa < b :
        xb = xa + h
        luas += ititiktengah(f, xa, xb)
        xa = xb
    return luas

def INC2(f, a, b, n=1):
    inc2 = lambda f, a, b:(b-a)/6 * (f(a) + 4 * f((a+b)/2) + f(b))
    xa = a; h = (b-a) / n;luas = 0
    for i in range(n):
        xb = xa + h
        luas += inc2(f, xa, xb)
        xa = xb
    return luas

def INC3(f, a, b, n=1):
    inc3 =  lambda f,a,b: (b-a)/8 * (f(a)+3*f((b-a)/3)+3*f((2*(b-a))/3)+f(b))
    xa = a; h = (b-a) / n;luas = 0
    for i in range(n):
        xb = xa + h
        luas += inc3(f, xa, xb)
        xa = xb
    return luas