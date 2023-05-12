def midTurunanDiskrit1(list_x, list_y) :
    h = list_x[1] - list_x[0]
    return (-1 * list_y[0] + list_y[2] ) / (2 * h)  

def midTurunanKontinu1(f,x, h):
    return (-1 * f(x-h) + f(x+h) ) / (2 * h)