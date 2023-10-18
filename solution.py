# Решения в работе
# KATA 5 - Penalty for speeding

import itertools
from functools import reduce


'''
def penalty(numbers):

    per = list(itertools.permutations(numbers))
    D = [int(reduce((lambda x, y: x + y), (p))) for p in per]
    return str(min(D))
'''

'''
def penalty(numbers):
    F = []

    for i in itertools.permutations(numbers):
        D = int(''.join([j for j in i]))
        F.append(D)
    return str(min(F))
'''


def penalty(numbers):
    F = []

    for i in itertools.permutations(numbers):
        D = int(''.join([j for j in i]))
        F.append(D)
    return str(min(F))


print(penalty(['100', '10', '1']))          # '100101'
print(penalty(['45', '30', '50', '1']))     # '1304550'
