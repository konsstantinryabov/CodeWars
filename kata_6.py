'''
# KATA 6 - Simple Fun #15: Addition without Carrying
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