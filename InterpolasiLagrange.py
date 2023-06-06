from rich import *
from rich.table import Table

def LagrangeFunction(x_input, x_index, x_list):
    n = len(x_list)
    hasil = 1
    for i in range(n):
        if i != x_index :
            hasil *= (x_input - x_list[i]) / (x_list[x_index] - x_list[i])
    return hasil

def InterpolasiLagrange(x_input, x_list, y_list):
    n = len(x_list)
    return sum( y_list[i] * LagrangeFunction(x_input,i, x_list) for i in range(n))

def StringLagrangeFunction(x_index, x_list):
    func = ''
    n = len(x_list)
    pertama = True
    
    for i in range(n):
        
        if i != x_index :
            if pertama == False : func += ' * '
            func +='((' + 'x' + ' - ' +  str(x_list[i]) + ') / ' + str(x_list[x_index] - x_list[i]) + ')' 
            pertama = False
        print("L :", i,":" , func)
    print('\n')
    return func

def StringInterpolasiLagrange(x_list, y_list, namafungsi = 'f'):
    func = namafungsi + ' = lambda x:'
    n = len(x_list)
    table = Table(title="Fungsi Lagrange")
    table.add_column("i", style="yellow")
    table.add_column("Y", style="blue")
    table.add_column("L", style="magenta")
    
    for i in range(n) :
        if i > 0 : func += ' + '
        table.add_row(str(i),str(y_list[i]), StringLagrangeFunction(i, x_list))
        func += '(' + str(y_list[i]) + ' * ' + StringLagrangeFunction(i, x_list) + ')'
        print(i, func, '\n')
    
    print(table)
    print("\n", func)
    return func

def stringInterpolasilagrangeClean(x_list, y_list, namafungsi = 'f'):
    func = namafungsi + ' = lambda x:'
    n = len(x_list)
    
    for i in range(n) :
        if i > 0 : func += ' + '
        func += '(' + str(y_list[i]) + ' * ' + StringLagrangeFunction(i, x_list) + ')'
        print(i, func, '\n')
    return func

def stringPembilangL(x_index, x_list):
    func = ''
    n = len(x_list)
    pertama = True
    for i in range(n):
        if i != x_index :
            if pertama == False : func += ' * '
            func +='(' + 'x' + ' - ' +  str(x_list[i]) + ')'
            pertama = False
    print('L('+ str(i) +')'+'=')
    return func