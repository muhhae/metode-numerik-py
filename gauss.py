def gauss(M):

    BO=[M[0][i]/M[0][0] for i in range(len(M[0]))]
    B1=[BO[i]*M[1][i]for i in range(len(M[0]))]
    for i in range(len(B1)):M[1][i]-=B1[i]

    B2=[BO[i]*M[2][i]for i in range(len(M[2]))]
    for i in range(len(B2)):M[2][i]-=B2[i]

    BO=[M[1][i]/M[1][1] for i in range(len(M[1]))]
    B2=[BO[i]*M[2][i]for i in range(len(M[2]))]

    for i in range(len(B2)):M[2][i]-=B2[i]

    X1 = M[2][3]/M[2][2]
    X2 = (M[1][3]-X1*M[1][2])/M[1][1]
    X3 = (M[0][3]-X1*M[0][2]-X2*M[0][1])/M[0][0]

    print(X1,X2,X3)
