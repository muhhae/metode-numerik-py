def ctk(M):
    for b in M:
        print(b)

def bbsrt(A):
    def labsc(H1,H2):
        h1=[abs(e) for e in H1]
        h2=[abs(e) for e in H2]
        return h1>h2
    n = len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if labsc(A[j],A[i]):A[i],A[j]=A[j],A[i]

def hasilX(baris,kolomX):
    hasil = baris[len(baris)-1]
    for i in range (len(baris)-1):
        if (i != kolomX):
            hasil -= baris[i]
    hasil /= baris[kolomX]
    return hasil

def gauss(A):
    bbsrt(A)
    for i in range(len(A)-1):
        pengurang = [A[i][j]/A[i][i] for j in range(len(A[i]))]
        for j in range(i+1, len(A)):
            A[j] = [A[j][k]-pengurang[k]*A[j][i] for k in range(len(A[i]))]
    print('\n')        
    ctk(A)
    for i in range (len(A)-1, -1, -1):
        print("\nX", i+1, '= ', hasilX(A[i], i))
        
