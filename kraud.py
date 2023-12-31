'''
# Задача 1
"""
Разработчик решил создать самый большой словарь в мире. Для
этого он придумал функцию biggest_dict, которая принимает
неограниченное количество параметров «ключ: значение» и обновляет
созданный им словарь my_dict, состоящий всего из одного элемента
«first_one» со значением «we can do it». Воссоздайте эту функцию.
"""

def biggest_dict(**kvargs):
    my_dict = {'first_one': 'we can do it'}
    my_dict.update(kvargs)
    return my_dict


print(biggest_dict(dog="Brock"))
print(biggest_dict(Лещ='2кг', Окунь='4кг', dog="Brock", ui=2, h=6789))


# Задача 2
"""
Напишите функцию to_dict, которая принимает аргумент в виде
списка и возвращает словарь, в котором каждый элемент списка
является и ключом и значением. Предполагается, что элементы
списка будут соответствовать правилам задания ключей в словарях.
"""

def to_dict(spi):
    return dict(zip(spi, spi))


print(to_dict([1, 2, 't', 'y', 'i']))
print(to_dict(['o', 2, 'qwerty', 'uiop', 'fghjk', 'ghjk']))
'''

# Задача 3
"""
Программная система, над которой работает Разработчик, состоит
из большого количества функций. Иногда функции не завершаются
возвратом ожидаемого результата, а выбрасывают исключение.
Повторный вызов функции с теми же аргументами может завершиться
ожидаемо. Для запуска в продакшен необходимо обеспечить
определённый уровень надёжности работы системы. Разработчик
планирует достичь требуемой надёжности следующим образом: при
возникновении исключения во время выполнения функции для
большинства функций повторять их вызов бесконечное количество
раз, а для пяти особенных функций - повторять вызов не более
трёх раз. Предложите инструмент и способ его применения для
реализации плана Разработчика.
"""
