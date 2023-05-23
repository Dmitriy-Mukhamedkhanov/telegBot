import random
def Game_stone_scissors_paper(name):
    dictionary = ['камень','ножницы','бумага']
    data = random.choice(dictionary)
    if name == 'камень' and data == 'камень':
        return 'ничья'
    elif name == 'камень' and data == 'ножницы':
        return 'Победа'
    elif name == 'камень' and data == 'бумага':
        return 'Проиграл'
    elif name == 'ножницы' and data == 'камень':
        return 'Проиграл'
    elif name == 'ножницы' and data == 'ножницы':
        return 'ничья'
    elif name == 'ножницы' and data == 'бумага':
        return 'Победа'
    elif name == 'бумага' and data == 'камень':
        return 'Победа'
    elif name == 'бумага' and data == 'ножницы':
        return 'Проиграл'
    elif name == 'бумага' and data == 'бумага':
        return 'ничья'
