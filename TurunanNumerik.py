def midTurunanKontinu(f, x, h, turunan_ke):
    K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0 : pembagi *= 2
    return sum(K[turunan_ke - 1][i] * f(x + ((i - 2) * h)) for i in range(5)) / pembagi

def forTurunanKontinu(f, x, h, turunan_ke):
    K = [[-3, 4, -1, 0, 0, 0], [2, -5, 4, -1, 0, 0], [-5, 18, -24, 14, -3, 0], [3, -14, 26, -24, 11, -2]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0 : pembagi *= 2
    return sum(K[turunan_ke - 1][i] * f(x + i * h) for i in range(6)) / pembagi

def backTurunanKontinu(f, x, h, turunan_ke):
    K = [[0, 0, 0, 1, -4, 3], [0, 0, -1, 4, -5, 2], [0, 3, -14, 24, -18, 5], [-2, 11, -24, 26, -14, 3]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0 : pembagi *= 2
    return sum(K[turunan_ke - 1][i] * f(x + (i - 5) * h) for i in range(6)) / pembagi

def midTurunanDiskrit(x_index, list_x, list_y, turunan_ke):
    h = list_x[1] - list_x[0]
    K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0: pembagi *= 2
    return sum(K[turunan_ke - 1][i] * list_y[x_index + i - 2] for i in range(5)) / pembagi

def forTurunanDiskrit(x_index, list_x, list_y, turunan_ke):
    h = list_x[1] - list_x[0]
    K = [[-3, 4, -1, 0, 0, 0], [2, -5, 4, -1, 0, 0], [-5, 18, -24, 14, -3, 0], [3, -14, 26, -24, 11, -2]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0: pembagi *= 2
    return sum(K[turunan_ke - 1][i] * list_y[x_index + i] for i in range(6)) / pembagi

def backTurunanDiskrit(x_index, list_x, list_y, turunan_ke):
    h = list_x[1] - list_x[0]
    K = [[0, 0, 0, 1, -4, 3], [0, 0, -1, 4, -5, 2], [0, 3, -14, 24, -18, 5], [-2, 11, -24, 26, -14, 3]]
    pembagi = h ** (turunan_ke)
    if turunan_ke % 2 != 0: pembagi *= 2
    return sum(K[turunan_ke - 1][i] * list_y[x_index + i - 5] for i in range(6)) / pembagi


# def midTurunanDiskrit(x_index, list_x, list_y, turunan_ke):
#     h = list_x[1] - list_x[0]
#     K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
#     pembagi = h ** (turunan_ke)
#     if turunan_ke % 2 != 0: pembagi *= 2
#     return (
#         (K[turunan_ke - 1][0] * list_y[x_index - 2] +
#          K[turunan_ke - 1][1] * list_y[x_index - 1] +
#          K[turunan_ke - 1][2] * list_y[x_index] +
#          K[turunan_ke - 1][3] * list_y[x_index + 1] +
#          K[turunan_ke - 1][4] * list_y[x_index + 2]) / pembagi)

# def midTurunanKontinu(f, x, h, turunan_ke):
#     K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
#     pembagi = h ** (turunan_ke)
#     if turunan_ke % 2 != 0 : pembagi *= 2
#     return (
#         (K[turunan_ke - 1][0] * f(x - 2 * h) +
#          K[turunan_ke - 1][1] * f(x - h) +
#          K[turunan_ke - 1][2] * f(x) +
#          K[turunan_ke - 1][3] * f(x + h) +
#          K[turunan_ke - 1][4] * f(x + 2 * h)) / pembagi)

# def forTurunanKontinu(f, x, h, turunan_ke):
#     K = [[-3, 4, -1, 0, 0, 0], [2, -5, 4, -1, 0, 0], [-5, 18, -24, 14, -3, 0], [3, -14, 26, -24, 11, -2]]
#     pembagi = h ** (turunan_ke)
#     if turunan_ke % 2 != 0 : pembagi *= 2
#     return (
#         (K[turunan_ke - 1][0] * f(x) +
#          K[turunan_ke - 1][1] * f(x + 1 * h) +
#          K[turunan_ke - 1][2] * f(x + 2 * h) +
#          K[turunan_ke - 1][3] * f(x + 3 * h) +
#          K[turunan_ke - 1][4] * f(x + 4 * h) +
#          K[turunan_ke - 1][5] * f(x + 5 * h)) / pembagi )
#
# def backTurunanKontinu(f, x, h, turunan_ke):
#     K = [[0, -1, 0, 1, 0], [0, 1, -2, 1, 0], [-1, 2, 0, -2, 1], [1, -4, 6, -4, 1]]
#     pembagi = h ** (turunan_ke)
#     if turunan_ke % 2 != 0 : pembagi *= 2
#     return (
#         (K[turunan_ke - 1][0] * f(x - 2 * h) +
#          K[turunan_ke - 1][1] * f(x - h) +
#          K[turunan_ke - 1][2] * f(x) +
#          K[turunan_ke - 1][3] * f(x + h) +
#          # K[turunan_ke - 1][4] * f(x + 2 * h)) / pembagi)



