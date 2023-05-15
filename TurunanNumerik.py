def midTurunanDiskrit(x_index, list_x, list_y, turunan_ke):
    h = list_x[1] - list_x[0]
    K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0: pembagi *= 2
    return (
        (K[turunan_ke - 1][0] * list_y[x_index - 2] +
         K[turunan_ke - 1][1] * list_y[x_index - 1] +
         K[turunan_ke - 1][2] * list_y[x_index] +
         K[turunan_ke - 1][3] * list_y[x_index + 1] +
         K[turunan_ke - 1][4] * list_y[x_index + 2]) / pembagi)

def midTurunanKontinu(f, x, h, turunan_ke):
    K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0 : pembagi *= 2 
    return (
        (K[turunan_ke - 1][0] * f(x - 2 * h) +
         K[turunan_ke - 1][1] * f(x - h) +
         K[turunan_ke - 1][2] * f(x) +
         K[turunan_ke - 1][3] * f(x + h) +
         K[turunan_ke - 1][4] * f(x + 2 * h)) / pembagi)