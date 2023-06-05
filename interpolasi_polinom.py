class interpolasi:
    def polinom(x,y):
        import acumalaka
        a=[[]for i in range(len(x))]
        for i in range (len(x)) :
            a[i]=[0 for j in range (len(x))]
        for j in range (len(x)) :
            for i in range(len(x)):
                a[j][i]=x[j]**i
        OBE=acumalaka.tambah(a,y)
        koef=acumalaka.OBE(OBE,len(x))
        fungsi="f=lambda x:0"
        for i in range(len(x)) :
            koef[i]=koef[i][len(x)]
            fungsi=fungsi+"+%f*x**%f"%(koef[i],i)
        return fungsi
    
    def newton(x,y):
        z=y
        a = [[] for i in range(len(x)-1)]
        for j in range (len(x)-1) :
            for i in range (len(x)-1-j) :
                a[j]+=[(z[i]-z[i+1])/(x[i]-x[i+j+1])]
        z=a[j]
        koef=[] 
        koef=[a[i][0] for i in range(len(x)-1)] 
        fungsi="f=lambda x:%f"%y[0]
        for i in range(len(x)-1):
            fungsi+="  +%f*(x-(%f))"%(koef[i],x[i])
            for j in range(i) :
                fungsi+="*(x-(%f))"%(x[j])
        return fungsi
    
    def langrang(x,y):
        fungsi = "f=lambda x: 0"
        for i in range(len(x)) :
            fungsi +=" + (%f)"%(y[i])
            for j in range(len(x)):
                if i!=j :
                    fungsi+="*((x-%f)/(%f-%f)"%(x[j],x[i],x[j])
    





