# KATA 7 - Nickname Generator
'''
def nickname_generator(name):
    """
    функция выводит сокращённое имя
    """

    if len(name) < 4:
        return "Error: Name too short"

    elif name[2] == 'y' or name[2] not in 'aeoiu':
        return name[:3]

    elif name[2] in 'aeoiu':
        return name[:4]


print(nickname_generator("Jimmy"))
print(nickname_generator("Samantha"))
print(nickname_generator("Sam"))
print(nickname_generator("Kayne"))
print(nickname_generator("Melissa"))
print(nickname_generator("James"))
'''


# KATA 7 - User class for Banking System
'''
class User(object):
    """С помощью класса можно:
    - снимать средства через метод: withdraw
    - пополнять баланс первому пользователю на сумму из баланса
    второго пользователя: check
    - пополнять баланс через метод: add_cash"""
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, su):
        """Это метод, который отвечает за снятие суммы с баланса."""
        if self.balance > su:
            self.balance = self.balance - su
            return f"{self.name} has {self.balance}."
        else:
            raise ValueError(f"{self.name} doesn't have enough money.")


    def check(self, nam, su):

        """"Этот метод добавляет сумму пользовалю который
        запрашивает и снимает эту сумму
        у второго пользователя, проверяет акаут
        второго пользователя на приватность,
        проверяет есть ли запрашиваемая сумма у второгопользователя."""
        if nam.balance < su:
            raise ValueError(f"{nam.name} can't withdraw {su},
                             he only has {nam.balance}.")
        if nam.checking_account == False:
            nam.checking_account = True
            raise ValueError(f"{nam.name} checking account is disabled.")
        else:
            self.balance = self.balance + su
            return f"{self.name} has {self.balance} and {nam.withdraw(su)}"

    def add_cash(self, su):
        """Этот метод позволяет внести сумму на баланс пользователя."""
        self.balance = self.balance + su
        return f"{self.name} has {'%.f' % self.balance}."
'''


# KATA 7 - First-Class Function Factory
'''
def factory(x):
    """
    Функция принимает число в качестве параметра и возвращает
    другую функцию, в которую передаём список.
    """
    z = x

    def my_array(g):
        return [i*z for i in g]
    return my_array


threes = factory(3)
print(threes([3, 6, 9]))
'''
