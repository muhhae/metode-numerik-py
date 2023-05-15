def list():
    print("\n ~~AkarSPLGauss function list~~ \n")
    print("ctk(M) \n\t- print list\n")
    print("bbsrt(A) \n\t- mengurutkan dari besar - kecil, absolute\n")
    print("gaussJordan(matrixKoef,matrixKonst) \n\t- eliminasi Gauss Jordan\n")
    print("gaussJordanHasil(matrixKoef, matrixKonst) \n\t- menghasilkan list dari solusi dengan eliminasi Gauss Jordan\n")
    print("gaussSaja(matrixKoef,matrixKonst) \n\t- Elimininasi Gauss\n")
    print("gaussSeidel(matrixKoef,matrixKonst,batasIterasi) \n\t- Gauss seidel\n")
    print("iterasiJacobi(matrixKoef,matrixKonst,batasIterasi) \n\t- iterasi jacobi\n")


def ctk(M):
    for b in M:
        print(b)
    print('\n')

def printBaris(A, newLine):
    for e in A:
        print(e,' ', end='')
    if newLine : print('\n')

def bbsrt(A):
    def labsc(H1,H2):
        h1=[abs(e) for e in H1]
        h2=[abs(e) for e in H2]
        return h1>h2
    n = len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if labsc(A[j],A[i]):A[i],A[j]=A[j],A[i]

def matrixTereduksi(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            barisEle = matrix[j]
            print("baris elementer = ", end='')
            printBaris(barisEle, True)
            print('baris ', i+1, 'dikurangi baris elementer * ', matrix[i][j],'\n') 
            matrix[i] = [matrix[i][k]-barisEle[k]*matrix[i][j] for k in range(len(matrix[i]))]
            ctk(matrix)


def hasilX(baris,kolomX, Arrhasil):
    hasil = baris[len(baris)-1]
    for i in range (len(baris)-1):
        if (i != kolomX):
            hasil -= baris[i]*Arrhasil[i]
    hasil /= baris[kolomX]
    return hasil

def OBE(A):
    for i in range(len(A)-1):
        bbsrt(A)
        print("Baris ", i+1,'dibagi ', A[i][i])
        A[i] = [A[i][j]/A[i][i] for j in range(len(A[i]))]
        ctk(A)
        print("baris elementer = ", end='')
        printBaris(A[i], True)
        for j in range(i+1, len(A)):
            print('baris ', j+1, 'dikurangi baris elementer * ', A[j][i],'\n') 
            A[j] = [A[j][k]-A[i][k]*A[j][i] for k in range(len(A[i]))]
            ctk(A)
    print("Baris ", len(A),'dibagi ', A[len(A)-1][len(A)-1])
    A[len(A)-1] = [A[len(A)-1][j]/A[len(A)-1][len(A)-1] for j in range(len(A[len(A)-1]))]
    ctk(A)
    
def gaussJordan(matrixKoef,matrixKonst):
    B = matrixKoef.copy()
    C = matrixKonst.copy()

    A = [B[i]+[C[i]] for i in range(len(B))]

    print("Matrix diurutkan dari tertinggi")
    bbsrt(A)
    ctk(A)
    OBE(A)
    matrixTereduksi(A)
    Arrhasil = [A[i][-1] for i in range(len(A))]
    for i in range (len(Arrhasil)):
        print("\nX(", i+1, ') = ', Arrhasil[i], sep='')

def gaussJordanHasil(matrixKoef, matrixKonst):
    B = matrixKoef.copy()
    C = matrixKonst.copy()

    A = [B[i]+[C[i]] for i in range(len(B))]

    print("Matrix diurutkan dari tertinggi")
    bbsrt(A)
    ctk(A)
    OBE(A)
    matrixTereduksi(A)
    Arrhasil = [A[i][-1] for i in range(len(A))]
    for i in range (len(Arrhasil)):
        print("\nX(", i+1, ') = ', Arrhasil[i], sep='')
    return Arrhasil

def gaussSaja(matrixKoef,matrixKonst):
    B = matrixKoef.copy()
    C = matrixKonst.copy()

    A = [B[i]+[C[i]] for i in range(len(B))]

    bbsrt(A)
    OBE(A)
    Arrhasil = [0]*(len(A[0])-1)
    for i in range (len(A)-1, -1, -1):
        Arrhasil[i] = hasilX(A[i], i, Arrhasil)
    for i in range (len(Arrhasil)):
        print("\nX(", i+1, ') = ', Arrhasil[i], sep='')
    return Arrhasil


def gaussSeidel(matrixKoef,matrixKonst,batasIterasi):

    iterasi = 0

    A = matrixKoef.copy()
    B = matrixKonst.copy()

    x = [0] * len(A)

    while True:
        iterasi += 1
        print("iterasi ", iterasi)
        x1p = x[0]
        for i in range(len(A)):
            x[i] = B[i]
            for j in range(len(A)):
                if j != i :
                    x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]
        print(x)
        print('\n')

        if x[0] != 0 : 
            error = abs((x1p-x[0])/x[0])
            print('error = ', error)

            if error < 1e-8 or (iterasi > batasIterasi) : break

            # if iterasi > 20 and error > error0 : break

def gaussSeidelHasil(matrixKoef,matrixKonst,batasIterasi):

    iterasi = 0

    A = matrixKoef.copy()
    B = matrixKonst.copy()

    x = [0] * len(A)

    while True:
        iterasi += 1
        print("iterasi ", iterasi)
        x1p = x[0]
        for i in range(len(A)):
            x[i] = B[i]
            for j in range(len(A)):
                if j != i :
                    x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]
        print(x)
        print('\n')

        if x[0] != 0 :
            error = abs((x1p-x[0])/x[0])
            print('error = ', error)

            if error < 1e-8  : break
        return x

def iterasiJacobi(matrixKoef,matrixKonst,batasIterasi):

    iterasi = 0

    A = matrixKoef.copy()
    B = matrixKonst.copy()

    x = [0] * len(A)
    xn = [0] * len(A)

    while True:
        iterasi += 1
        print("iterasi ", iterasi)
        for i in range(len(A)):
            xn[i] = B[i]
            for j in range(len(A)):
                if j != i :
                    xn[i] -= A[i][j] * x[j]
            xn[i] /= A[i][i]
        print(xn)
        print('\n')

        if x[0] != 0 :
            error = abs((xn[0]-x[0])/x[0])
            print('error = ', error)

            if error < 1e-8 or (iterasi > batasIterasi) : break



     
