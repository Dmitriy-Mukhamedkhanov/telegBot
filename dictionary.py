from random import choice

def DIC():
    dictionary = {'Вася': 'Вася Привет999','Коля':'Коля Привет','Маша':'Маша Привет',
               'Петя':'Петя привет'}
    return dictionary


def POE():
    dictionary = {'1': 'Тютчев,Вечер:\nКак тихо веет над долиной\nДалекий колокольный звон,\nКак шум от стаи журавлиной, —\nИ в звучных листьях замер он ....',
                  '2':'Тютчев,Весенняя гроза:\nЛюблю грозу в начале мая,\nКогда весенний, первый гром,\nКак бы резвяся и играя,\nГрохочет в небе голубом.',
                  '3':'Тютчев,Весенние воды:\nЕще в полях белеет снег,\nА воды уж весной шумят-\nБегут и будят сонный брег,\nБегут и блещут и гласят…'}
    data = choice(list(dictionary.items()))
    return data

def POE_PUSHKIN():
    dictionary_push = {
        '1': 'Пушкин,Дружба:\nЧто дружба? Легкий пыл похмелья,\nОбиды вольный разговор,\nОбмен тщеславия, безделья\nИль покровительства позор.',
        '2': 'Пушкин,Городок:\nПрости мне, милый друг,\nДвухлетнее молчанье:\nПисать тебе посланье\nМне было недосуг...',
        '3': 'Пушкин,Приятелю:\nНе притворяйся, милый друг,\nСоперник мой широкоплечий!\nТебе не страшен лиры звук,\nНи элегические речи.…'}
    data = choice(list(dictionary_push.items()))

    return data
