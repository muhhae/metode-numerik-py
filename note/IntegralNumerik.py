def list():
    print("Trapesium(f, a, b, n=1):")
    print("Titiktengah(f, a, b, n=1):")

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