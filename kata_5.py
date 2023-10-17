# KATA 5 - Count IP Addresses
'''
def Funkc(ip1, ip2):
    """
    Функция расчитывает количесно IP адресов между первым и вторым IP адресами.
    - принимает 2 строковых аргумента
    - возвращает int значение колличества IP адресов
    """
    IP1 = [int(x) for x in ip1.split('.')]
    IP2 = [int(x) for x in ip2.split('.')]

    def MAX(ip):
        return ip[3] + (256 * ip[2]) + ((256 * 256) * ip[1]) + (((256 *
        256) * 256) * ip[0])

    return MAX(IP2) - MAX(IP1)

print(Funkc("10.0.0.0", "10.0.0.50"))
print(Funkc("10.0.0.0", "10.0.1.0"))
print(Funkc("20.0.0.10", "20.0.1.0"))

# ещё вариант
from ipaddress import ip_address
def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


# ещё вариант
def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)
'''


# KATA 5 - First non-repeating character
'''
def first_non_repeating_letter(x):
    """
    Функция возвращает первый не повторяющийся элемент в стркое.
    """
    if x == '':
        return ''
    s = x.lower()
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return x[i]
        elif i+1 == len(s):
            return ''
'''


# KATA 5 - Human Readable Time
'''
def make_readable(x):
    """
    Функция переводит секунды в обычный формат отображения времени ЧЧ:ММ:СС.
    """
    ch = x // 3600  #полные часы
    mn = x % 3600 // 60 #полные минуты
    sk = x % 3600 % 60 # секунды
    return '{:02d}:{:02d}:{:02d}'.format(ch, mn, sk)
'''


# KATA 5 - Moving Zeros To The End
'''
def move_zeros(lst):
    """
    Функция перемещает все нули в конец списка не меняя порядок
    остальных чисел.
    """
    for i in lst:
        if i == 0:
            lst.remove(i) # Remove the element from the array
            lst.append(i) # Append the element to the end
    return lst

# ещё вариант
def move_zeros(x):
    if len(x) == 0 or len(x) == x.count(0):
        return x
    else:
        a = []
        i = 0
        while x.count(0) != 0:
            if x[i] == 0:
                a.append(x[i])
                del x[i]
                i -= 1
            i += 1
        else:
            return x + a
'''


# KATA 5 - Ninja vs Samurai: Attack + Block
'''
Position = {'high': 'h', 'low': 'l'}

class Warrior(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ''
        self.deceased = self.zombie = False

    @staticmethod
    def attack(enemy, position):
        damage = 0
        if enemy.block != position:
            damage += (5, 10)[position == 'h']
        if enemy.block == '':
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        if new_health == 0:
            self.deceased = True
            self.zombie = False
        elif self.deceased:
            self.zombie = True
        self.health = max(0, new_health)
'''


# KATA 5 - Rotate an array matrix
'''
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

# ещё вариант
import numpy as np
d = {"clockwise":3, "counter-clockwise":1}

def rotate(matrix, direction):
    return np.rot90(matrix, d[direction]).tolist()


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
'''
