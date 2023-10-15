'''
# KATA 5 - Count IP Addresses
def Funkc(ip1, ip2):
    """
    Функция расчитывает количесно IP адресов между первым и вторым IP адресами.
    - принимает 2 строковых аргумента
    - возвращает int значение колличества IP адресов
    """
    IP1 = [int(x) for x in ip1.split('.')]
    IP2 = [int(x) for x in ip2.split('.')]

    def MAX(ip):
        return ip[3] + (256 * ip[2]) + ((256 * 256) * ip[1]) + (((256 * 256) * 256) * ip[0])

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