ft1cd = lambda yy,h : (yy[2] - yy[0]) / (2 * h)
ft1cc = lambda f,x,h: ft1cd ([f(x-h) , 0 ,f(x+h)],h)
ft1rd = lambda yy, h:(yy[1] - yy[0])/h
ft1rc = lambda f, x, h: ft1rd([f(x), f(x+h)], h)
ft2cd = lambda f, x, h:
