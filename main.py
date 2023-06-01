
import telebot
import dictionary
from telebot import types
import button
import time
import csv
import Game

from config import TOTAL_WIN, TOTAL_DRAW, TOTAL_LOSE, TOTAL_WIN_ADMIN, TOTAL_DRAW_ADMIN, TOTAL_LOSE_ADMIN, ID_ADMIN,\
    dictionary_total, API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    if message.from_user.id == ID_ADMIN:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создание клавы
        markup.row('Поэзия', 'Игра')
        markup.row('ТОП-игроков')
        bot.reply_to(message, "Howdy, how are you doing?",reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создание клавы
        markup.row('Поэзия', 'Игра')
        bot.reply_to(message, "Howdy, how are you doing?", reply_markup=markup)


@bot.message_handler(content_types='text')
def start_message(message):
    name_dic = dictionary.DIC()
    if message.text in name_dic:
        bot.send_message(message.from_user.id, name_dic[message.text])
    elif message.text == "Что делать?":\
        bot.send_message(message.from_user.id, "Напиши что-нибудь?")
    elif message.text == "Поэзия": \
        send_welcome(message)
        # bot.send_message(message.from_user.id, send_welcome(message))
    elif message.text == "Игра" : \
        send_Game(message)
        # bot.send_message(message.from_user.id, send_Game(message))
    elif message.text == "ТОП-игроков" : \
        top_players(message)
        # bot.send_message(message.from_user.id, top_players(message))
    else:
        print(message.from_user.id)
        bot.send_message(message.chat.id, f"я не знаю что ответить на: {message.text} ")
        bot.send_message(message.chat.id, "Вы можете написать боту запросы в следующем формате:"
                                          "Напиши имя:\n Вася,\n Петя,\n Коля,\n Маша,\n Петя\n или"
                                          " команды /start, /help, /Game\n"
                                          "для поэзии набери команду /poetry")


@bot.message_handler(ccommands=['Game'])  # Если сообщение = Поэзия, то ...
def send_Game(message):
    if message.from_user.id == ID_ADMIN:
        markup_in = types.InlineKeyboardMarkup()  # Создание клавы инлайн
        button1 = types.InlineKeyboardButton('🤜', callback_data='button1')
        button2 = types.InlineKeyboardButton('✂️', callback_data='button2')
        button3 = types.InlineKeyboardButton('◽️', callback_data='button3')
        button4 = types.InlineKeyboardButton('Общий Сброс', callback_data='button4')
        button5 = types.InlineKeyboardButton('Сброс', callback_data='button5')
        button6 = types.InlineKeyboardButton('Общая статистика', callback_data='button6')
        markup_in.add(button1, button2, button3, button4, button5, button6)
        bot.reply_to(message,f"Играет АДМИН: {message.from_user.first_name}", reply_markup=markup_in)
    else:
        markup_in = types.InlineKeyboardMarkup()  # Создание клавы инлайн
        button1 = types.InlineKeyboardButton('🤜', callback_data='button1')
        button2 = types.InlineKeyboardButton('✂️', callback_data='button2')
        button3 = types.InlineKeyboardButton('◽️', callback_data='button3')
        button5 = types.InlineKeyboardButton('Сброс', callback_data='button5')
        button6 = types.InlineKeyboardButton('Общая статистика', callback_data='button6')
        markup_in.add(button1, button2, button3, button5, button6)
        bot.reply_to(message, f"Играет Пользователь: {message.from_user.first_name}", reply_markup=markup_in)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True) # Привязка кнопок btn1 и btn2
def callback_inline(call):
    global TOTAL_WIN, total
    global TOTAL_DRAW
    global TOTAL_LOSE
    global TOTAL_WIN_ADMIN
    global TOTAL_DRAW_ADMIN
    global TOTAL_LOSE_ADMIN
    global dictionary_total

    if call.data == 'btn1': # data это ???????????
        name_poetry = dictionary.POE()
        bot.send_message(call.message.chat.id, name_poetry[1])
    elif call.data == 'btn2':
        name_poetry = dictionary.POE_PUSHKIN()
        bot.send_message(call.message.chat.id, name_poetry[1])
    elif call.data == 'button1':
        stone = Game.Game_stone_scissors_paper('камень')
        bot.send_message(call.message.chat.id, stone)
        total = stone
    elif call.data == 'button2':
        cissors = Game.Game_stone_scissors_paper('ножницы')
        bot.send_message(call.message.chat.id, cissors)
        total = cissors
    elif call.data == 'button3':
        paper = Game.Game_stone_scissors_paper('бумага')
        bot.send_message(call.message.chat.id, paper)
        total = paper
    elif call.data == 'button4':
        TOTAL_WIN = 0
        TOTAL_DRAW = 0
        TOTAL_LOSE = 0
        bot.send_message(call.message.chat.id, 'Общий сброс произведен')
    elif call.data == 'button5':
        bot.send_message(call.message.chat.id, 'Сброс Себя')
        TOTAL_WIN_ADMIN = 0
        TOTAL_DRAW_ADMIN = 0
        TOTAL_LOSE_ADMIN = 0
    elif call.data == 'button6':
        total_number_win = TOTAL_WIN_ADMIN + TOTAL_WIN
        total_number_draw = TOTAL_DRAW_ADMIN + TOTAL_DRAW
        total_number_lose = TOTAL_LOSE_ADMIN + TOTAL_LOSE
        total_number_games = total_number_win + total_number_draw + total_number_lose
        bot.send_message(call.message.chat.id, f'общее кол-во всех побед: {total_number_win}')
        bot.send_message(call.message.chat.id, f'общее кол-во всех ничьих: {total_number_draw}')
        bot.send_message(call.message.chat.id, f'общее кол-во всех проигрышей: {total_number_lose}')
        bot.send_message(call.message.chat.id, f'итого игр: {total_number_games}')
    elif call.data == 'ТОП-игроков':
        top_players(call.message)


    if call.from_user.id == ID_ADMIN:
        dictionary_total[call.from_user.id] = {}
        # print(call.message.chat.id)
        # print(call.from_user.id)
        # print(ID_ADMIN)
        if total == 'Победа':
            if call.from_user.id not in dictionary_total:
                TOTAL_WIN = 0
                dictionary_total[call.from_user.id]['Победа'] = TOTAL_WIN
            else:
                TOTAL_WIN += 1
                dictionary_total[call.from_user.id]['Победа'] = TOTAL_WIN
        elif total == 'ничья':
            if call.from_user.id not in dictionary_total:
                TOTAL_DRAW = 0
                dictionary_total[call.from_user.id]['ничья'] = TOTAL_DRAW
            else:
                TOTAL_DRAW += 1
                dictionary_total[call.from_user.id]['ничья'] = TOTAL_DRAW
        elif total == 'Проиграл':
            if call.from_user.id not in dictionary_total:
                TOTAL_LOSE = 0
                dictionary_total[call.from_user.id]['Проиграл'] = TOTAL_LOSE
            else:
                TOTAL_LOSE += 1
                dictionary_total[call.from_user.id]['Проиграл'] = TOTAL_LOSE
    else:
        if total == 'Победа':
            TOTAL_WIN += 1
            dictionary_total[call.message.chat.id]['Победа'] = TOTAL_WIN
        elif total == 'ничья':
            TOTAL_DRAW += 1
            dictionary_total[call.message.chat.id]['ничья'] = TOTAL_DRAW
        elif total == 'Проиграл':
            TOTAL_LOSE += 1
            dictionary_total[call.message.chat.id] ['Проиграл'] = TOTAL_LOSE

    print(call.message.from_user.id) # Что это ???????



def top_players(message):
    global dictionary_total
    id_user = message.from_user.id
    name_user = message.from_user.username
    player_name = message.from_user.first_name

    bot.reply_to(message, id_user)
    bot.reply_to(message, name_user)
    bot.reply_to(message, player_name)

    print('Словарь')
    print(dictionary_total[id_user])


    save_data(dictionary_total,id_user)

def save_data(dictionary_total, id_user):
    with open('filename.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dictionary_total.items())








# Обработчик нажатий на кнопки
@bot.message_handler(commands=['poetry'])
def send_welcome(message):
    markup_in = types.InlineKeyboardMarkup() # Создание клавы инлайн
    btn1 = types.InlineKeyboardButton('Стихи Тютчева', callback_data='btn1')
    btn2 = types.InlineKeyboardButton('Стихи Пушкина', callback_data='btn2')
    markup_in.add(btn1, btn2)

    bot.reply_to(message, 'Минутка поэзии',reply_markup=markup_in) # здесь name_poetry[1] выводится на экран


while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка {e}")
        time.sleep(15)