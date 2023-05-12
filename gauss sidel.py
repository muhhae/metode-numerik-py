def siedel (A,B):
    x1,x2,x3,x4=0,0,0,0
    x1a = lambda x2,x3,x4: (B[0]-A[0][1]*x2-A[0][2]*x3-A[0][3]*x4)/A[0][0]
    x2a = lambda x1,x3,x4: (B[1]-A[1][0]*x1-A[1][2]*x3-A[1][3]*x4)/A[1][1]
    x3a = lambda x1,x2,x4: (B[2]-A[2][0]*x1-A[2][1]*x2-A[2][3]*x4)/A[2][2]
    x4a = lambda x1,x2,x3: (B[3]-A[3][0]*x1-A[3][1]*x2-A[3][2]*x3)/A[3][3]
    while True :
        x1p=x1
        x1=x1a(x2,x3,x4)
        x2=x2a(x1,x3,x4)
        x3=x3a(x1,x2,x4)
        x4=x4a(x1,x2,x3)
        print(x1,x2,x3,x4)
        if x1!=0 and abs((x1p-x1)/x1)<1e-8:break
    
    #lantai 

A=[[8,2,3,2],[2,9,-1,-2],[1,6,4,0],[1,3,2,-1]]
B=[0,1,3,2]

siedel(A,B)
##jacobi
#while True :
#    x1n=x1a(x2,x3)
 #   x2n=x2a(x1,x3)
  #  x3n=x3a(x1,x2)
   # print(x1n,x2n,x3n)
    #if abs((x1n-x1)/x1)<1e-4:break
    #x1,x2,x3=x1n,x2n,x3n

#kalau gaus sidel
#while True :
 #   x1p=x1
  #  x1=x1a(x2,x3)
  #  x2=x2a(x1,x3)
  #  x3=x3a(x1,x2)
  # print(x1,x2,x3)
  #  if x1!=0 and abs((x1p-x1)/x1)<1e-8:break
  #  x1,x2,x3=x1n,x2n,x3n