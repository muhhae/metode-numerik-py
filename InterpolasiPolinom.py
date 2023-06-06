from AkarSPLGauss import *
from rich import *

def list():
    print("\n~~InterpolasiPolinom Function List~~\n")
    print("interpolasi(matrix_x, matrix_y, nama_fungsi = 'f') \n\t- mendapatkan fungsi dari data x dan y dengan interpolasi polinomial\n")
    print("RegresiPolinom(x, y, orde, f = "f"):")
    print("def InterpolasiNewton(x, y, f = "f"):")

def getFunc(hasil, f = 'f'):
    ff = f + "=lambda z:"
    for i in range(len(hasil)):
        ff = ff + "(" + str(hasil[i]) + ")*z**" + str(i)
        if i < len(hasil) - 1:
            ff = ff + "+"

    print(ff)
    return ff

def InterpolasiPolinom(matrix_x, matrix_y, nama_fungsi="f"):
    m = [[matrix_x[i] ** j for j in range(len(matrix_x))] for i in range(len(matrix_x))]
    ctk(m)
    
    return getFunc(gaussJordanHasil(m, matrix_y), nama_fungsi)

def RegresiPolinom(x, y, orde, f = "f"):
    m = [[0] * (orde + 1)] * (orde + 1)
    m[0][0] = len(x)
    for i in range(1, orde + 1):
        m[0][i] = sum([a**i for a in x])
    for i in range(1, orde + 1):
        m[i] = [sum([a**j for a in x]) for j in range(i, orde + i + 1)]    
    ctk(m)
    
    my = [sum(x[j]**i * y[j] for j in range(len(x))) for i in range(orde + 1)]
    ctk(my)  
    
    return getFunc(gaussJordanHasil(m, my), f)

def InterpolasiNewton(x, y, f = "f"):
    z = y
    a = [[] for i in range(len(x) - 1)]
    for j in range (len(x) - 1) :
        for i in range (len(x) - 1 - j) :
            a[j] += [(z[i] - z[i + 1]) / (x[i] - x[i + j + 1])]
            
    z = a[j]
    
    koef = [a[i][0] for i in range(len(x) - 1)] 
    
    fungsi = f + "= lambda x:" + str(y[0])
    for i in range(len(x)-1):
        fungsi += " + " + str(koef[i]) + " * (x - " + str(x[i]) + ")"
        for j in range(i) :
            fungsi += " * (x - " + str(x[j]) + ")"
    return fungsi
