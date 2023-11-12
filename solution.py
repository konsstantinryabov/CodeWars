# Решения в работе
# KATA 5 - US Postal Codes

'''
D = []
F = []
with open("f.txt", "r") as file:
    D.append(file.readlines())
for i in D[0]:
    F.append(i[0:-1])
print(F)
'''


def Fu(USA):
    G = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
         'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
         'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
         'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
         'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
         'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
         'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
         'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
         'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
         'West Virginia', 'Wisconsin', 'Wyoming', 'District of Columbia',
         'American Samoa', 'Guam', 'Northern Mariana Islands', 'Puerto Rico',
         'U.S. Virgin Islands']
    F = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
         'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
         'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
         'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
         'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC', 'AS', 'GU', 'MP', 'PR',
         'VI']
    return "".join([i[1] for i in zip(G, F) if i[0] == USA])


print(Fu("Alabama"))
print(Fu("District of Columbia"))
print(Fu("U.S. Virgin Islands"))
print(Fu("Puerto Rico"))

# KATA 5 - Penalty for speeding

# import itertools
# from functools import reduce

# Вариант 1
'''
def penalty(numbers):
    per = list(itertools.permutations(numbers))
    D = [int(reduce((lambda x, y: x + y), (p))) for p in per]
    return str(min(D))
'''
# Вариант 2
'''
def penalty(numbers):
    F = []
    for i in itertools.permutations(numbers):
        D = int(''.join([j for j in i]))
        F.append(D)
    return str(min(F))
'''
# Вариант 3
'''
def Fu(numbers):
    for i in itertools.permutations(numbers):
        yield int(''.join([j for j in i]))
def penalty(numbers):
    return str(min([i for i in Fu(numbers)]))
'''
# Вариант 4
'''
def Fu(numbers):
    if len(numbers) == 1:
        yield (numbers[0], )
    else:
        for perm in Fu(numbers[1:]):
            for i in range(len(numbers)):
                yield perm[:i] + (numbers[0], ) + perm[i:]

def penalty(numbers):
    F = []
    for i in Fu(numbers):
        D = int(''.join([j for j in i]))
        F.append(D)
    return str(min(F))
'''

# Вариант 5 не закончено
'''

def penalty(numbers, ch):
    print(f'Входящие данные {numbers}')
    Len = []
    SPIS = []
    for i in numbers:
        Len.append(len(i))
    Max = max(Len)
    print(Max)
    for j in numbers:
        while True:
            if Max == len(j):
                SPIS.append(int(j))
                break
            elif Max > len(j):
                j = '0' + j

    print(sorted(SPIS))

print(penalty(['100', '10', '1'], '100101'))                                        # '100101'
print(penalty(['45', '30', '50', '1'], '1304550'))                                  # '1304550'
print(penalty(['32', '3'], '323'))                                                  # '323'
print(penalty(['70', '46', '4', '19'], '1944670'))                                  # '1944670'
print(penalty(['71', '82', '42', '34', '90'], '3442718290'))                        # '3442718290'
print(penalty(['31', '97', '6', '78'], '3167897'))                                  # '3167897'
print(penalty(['72', '7', '7', '78', '79', '709', '94'], '7097277787994'))          # '7097277787994'
'''