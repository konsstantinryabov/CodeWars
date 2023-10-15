'''
# KATA 7 - Nickname Generator
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