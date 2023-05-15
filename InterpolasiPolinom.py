from AkarSPLGauss import *

def list():
    print("\n~~InterpolasiPolinom Function List~~\n")
    print("interpolasi(matrix_x, matrix_y, nama_fungsi = 'f') \n\t- mendapatkan fungsi dari data x dan y dengan interpolasi polinomial\n")
    print("regresi(orde, matrix_x, matrix_y, nama_fungsi = 'f')\n")

def interpolasi(matrix_x, matrix_y, nama_fungsi = 'f') :
    m = [[matrix_x[i]**j for j in range(len(matrix_x))]for i in range(len(matrix_x))]
    ctk(m)
    hasil = gaussJordanHasil(m, matrix_y)
    ff = nama_fungsi + '=lambda z:'
    for i in range(len (hasil)):
        ff = ff+'('+str(hasil[i])+')*z**'+str(i)
        if i < len(hasil) -1:
            ff = ff+'+'
    return ff

def regresi(orde, matrix_x, matrix_y, nama_fungsi = 'f') :
    m = [[0] * (orde+1)] * (orde+1)
    m[0] = [orde] + [sum([matrix_x[i]**j for i in range (len(matrix_x))]) for j in range(1, orde+1)]
    for l in range(1, orde+1):
        m[l] = [sum([matrix_x[i]**j for i in range (len(matrix_x))]) for j in range(l, orde+1+l)]
    ctk(m)
    my = [sum([(matrix_x[i]**j)*matrix_y[i] for i in range(len(matrix_x))]) for j in range(orde+1)]
    ctk(my)

    hasil = gaussJordanHasil(m, my)

    ff = nama_fungsi + '=lambda z:'
    for i in range(len(hasil)):
        ff = ff + '(' + str(hasil[i]) + ')*z**' + str(i)
        if i < len(hasil) - 1:
            ff = ff + '+'
    return ff


    