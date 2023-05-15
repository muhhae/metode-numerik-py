def midTurunanDiskrit1(list_x, list_y):
    h = list_x[1] - list_x[0]
    return (-1 * list_y[0] + list_y[2]) / (2 * h)


def midTurunanKontinu(f, x, h, turunan_ke):
    K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0 : pembagi *= 2 
    return (
        (K[turunan_ke - 1][0] * f(x - 2 * h) +
         K[turunan_ke - 1][1] * f(x - h) +
         K[turunan_ke - 1][2] * f(x) + K[turunan_ke - 1][3] * f(x + h) +
         K[turunan_ke - 1][4] * f(x + 2 * h)) / pembagi )
