# Решения в работе
# KATA 5 - Rotate an array matrix

def rotate(matrix, direction):
    """
    Функция переворачивает матрицу на 90
    градусов либо по - 'clockwise',
    либо против часовой - 'counter-clockwise'
    - matrix - матрица списков
    - direction - угол
    """
    D = []
    if direction == 'clockwise':
        G = list(reversed(matrix))
        for i in range(len(matrix[0])):
            D.append([spisok[i] for spisok in G if i < len(spisok)])
        return list(filter(None, D))

    elif direction == 'counter-clockwise':
        for i in range(len(matrix[0])):
            D.append([spisok[i] for spisok in matrix if i < len(spisok)])
        return list(reversed(list(filter(None, D))))

print(rotate([[17, 6, -2, -4, -3],
              [6, 4, -15, 14, -11],
              [-12, 16, -1, -18, 3],
              [-18, 17, -16, -19, 8],
              [-9, -4, 16, -13, -13]], 'counter-clockwise'))

print(rotate([[17, 6, -2, -4, -3],
              [6, 4, -15, 14, -11]], 'clockwise'))


print(rotate([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], 'counter-clockwise'))

print(rotate([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], 'clockwise'))

print(rotate([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]], 'counter-clockwise'))

print(rotate([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]], 'clockwise'))
