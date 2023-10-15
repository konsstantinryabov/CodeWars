# KATA 6 - Simple Fun #15: Addition without Carrying
'''
def addition_without_carrying(a, b):
    """
    Функуия складывает столбиком но не переносит число влево.
    """

    a, b = str(a)[::-1], str(b)[::-1]

    if len(a) > len(b): z = len(a) - (len(a) - len(b))
    elif len(a) < len(b): z = len(b) - (len(b) - len(a))
    else: z = len(a)

    sum = ''.join(str(int(a[i]) + int(b[i]))[-1] for i in range(z))

    if len(a) > len(b): sum += a[z:]
    elif len(a) < len(b): sum += b[z:]

    return int(sum[::-1])

print(addition_without_carrying(56747, 674))      #56311
print(addition_without_carrying(456, 1734))       #1180
print(addition_without_carrying(99999, 0))        #99999
print(addition_without_carrying(999, 999))        #888
print(addition_without_carrying(0, 0))            #0
'''


# KATA 6 - Find The Parity Outlier
'''
def find_outlier(x):
    """
    Функция возвращает четное число из списка
    нечетных или нечетное из списка четных.
    """
    res_1 = list(filter(lambda i: i % 2 != 0, x))
    res_2 = list(filter(lambda i: i % 2 == 0, x))
    if len(res_1) == 1:
        return int(''.join(map(str, res_1)))
    return int(''.join(map(str, res_2)))
'''


# KATA 6 - Counting Duplicates
'''
def duplicate_count(x):
    """
    функцию возвращает количество различных букв и чисел,
    которые встречаются более одного раза.
    """
    d={}
    x = x.lower()
    for i in x:
        if x.count(i) > 1:
            d[i] = x.count(i)
    return len(d)
'''


# KATA 6 - Persistent Bugger.
'''
import functools as f
def persistence(x):
    d = len(str(x))
    i = 0
    if d == 1:
        return 0
    while d > 1:
        i += 1
        a = [int(i) for i in list(str(x))]
        x = f.reduce((lambda a, b: a * b), a)
        d = len(str(x))
        if d < 2:
            return i
'''


# KATA 6 - Stop gninnipS My sdroW!
'''
def spin_words(sentence):
    return ' '.join(map((lambda d: d[::-1] if len(d) > 4 else d), sentence.split()))
'''


# KATA 6 - Sum of Digits / Digital Root
'''
def digital_root(n):
    y = sum(list(map(int, str(n))))
    if y >= 10: return digital_root(y)
    else: return y
'''


# KATA 6 - Find the odd int
'''
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

# ещё вариант
def find_it(seq):
    for i in range(len(seq)):
        diigit = 0
        number = 0
        for j in range(i, len(seq)):
            if seq[j] not in seq[:i] and seq[i] == seq[j]:
                number += 1
                diigit = seq[i]
        if number % 2 != 0:
            return diigit
'''


# KATA 6 - Tribonacci Sequence
'''
def tribonacci(signature, n):  # нахождение чисел  трибоначчи
    if n == 0: return []
    elif n == 1: return [signature[0]]
    elif n == 2: return [signature[0],signature[1]]
    elif n >= 3:
        for i in range(n-3):
            signature.append(signature[i] + signature[i + 1] + signature[i + 2])
        return signature
'''


# KATA 6 - N-th Fibonacci
'''
def nth_fib(n):
    if n == 1:  return 0
    if n == 2:  return 1
    if n > 2:
        f1 = f2 = 1
        for i in range(2, n):
            f1, f2 = f2, f1 + f2
        return f1
'''


# KATA 6 - Who likes it?
'''
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

# ещё вариант
def likes(names):
    if len(names) == 0:    
        return 'no one likes this'
    if len(names) == 1:  
        return '{} likes this'.format(names[0])
    if len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    if len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    if len(names) >= 4:
        names_2 = names[2:]
        return '{}, {} and {} others like this'.format(names[0], names[1],
                                                       len(names_2))
'''


# KATA 6 - Create Phone Number
'''
def create_phone_number(n):
    str1 =  ''.join(str(x) for x in n[0:3])
    str2 =  ''.join(str(x) for x in n[3:6])
    str3 =  ''.join(str(x) for x in n[6:10])
    return '({}) {}-{}'.format(str1, str2, str3)

# ещё вариант
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# ещё вариант
def create_phone_number(n):
    row = '('
    for i in n:
        row+=str(i)
        if len(row) == 4:
            row+=') '            
        if len(row) == 9:
            row+= '-'
    return row
'''


# KATA 6 - 1RM Calculator
'''
def calculate_1RM(w, r):
    s = []
    s.append(w * (1 + r / 30))
    s.append((100 * w) / (101.3 - 2.67123 * r))
    s.append(w * (r ** 0.1))
    if r != 1 and r != 0:
        return round(max(s))
    elif r == 1:
        return w
    return 0
'''

# KATA 6 - Roman Numerals Encoder
'''
def solution(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
        print('({}) {} => {}'.format(roman, n, result))
    return result
'''


# KATA 6 - Multiples of 3 or 5
'''
def solution(number):
    return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])
'''


# KATA 6 - Round and Round
'''
from decimal import Decimal, ROUND_HALF_UP
def round_by_2_decimal_places(n):
    number = Decimal(n)
    return number.quantize(Decimal("1.00"), ROUND_HALF_UP)
'''


# KATA 6 - Does my number look big in this?
'''
def narcissistic( value ):
    n = str(value)
    g = 0
    for i in n: g += int(i) ** len(n)
    if g == value: return True
    else: return False
'''


# KATA 6 - Find the unique number
'''
def find_uniq(arr):
    for u in range(len(arr)):
        if arr[u] == arr[u-1]:
            continue
        if u != 0 and arr[u] != arr[u-1] or arr[u] != arr[u+1]:            
            break
    return arr[u]

# ещё вариант
def find_uniq(arr):
    for u in range(len(arr)):
        if arr[u] == arr[u-1]:
            continue
        if u != 0 and arr[u] != arr[u-1] or arr[u] != arr[u+1]:            
            break
    return arr[u]

# ещё вариант
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
'''


# KATA 6 - Breaking search bad
'''
def search(titles, term): 
    return list(filter(lambda title: term in title.lower(), titles))

# ещё вариант
def search(titles, term):
    return list(filter(lambda title: term in title.lower() , titles))
'''


# KATA 6 - Convert string to camel case
'''
def to_camel_case(s):
    #a = [i.upper() for i in s if i == '-' or i == '_']
    l = ''
    s2 = ''
    z = 0
    for i in s:
        z += 1
        if l == i.upper():
            l = ''
            continue        
        if '-' != i and '_' != i:
            s2 += i
        if i == '-' or i == '_':
            l = s[z].upper()
            s2 += l
    return s2
'''


# KATA 6 - Inserting multiple strings into another string
'''
def insert_at_indexes(phrase, word, indexes):
    for i in reversed(indexes):
        phrase = phrase[:i] + word + phrase[i:]
    return phrase
'''


# KATA 6 - Array.diff
'''
def array_diff(a, b):
    return ([elem for elem in a if elem not in b])

# ещё вариант
    c = []
    for elem_1 in a:
        if elem_1 in b:
            continue
        else:
            c.append(elem_1)
    return c
'''
