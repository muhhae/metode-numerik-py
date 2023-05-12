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

