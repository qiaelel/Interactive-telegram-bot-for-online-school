import config
import _sqlite3
from telebot import TeleBot, callback_data, types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


token = config.token
admin = config.admin

bot = TeleBot(token, parse_mode='MARKDOWN')
print("Бот запущен.")
print("Здесь будут отображаться логи:")

#кнопка возврата в главное меню
backinline = types.InlineKeyboardMarkup(row_width=1)
backinline_types = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back')
backinline.add(backinline_types)

#главная страница
@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    kb = types.InlineKeyboardMarkup(row_width=1)
    schedule = types.InlineKeyboardButton(text='Просмотреть расписание', callback_data='schedule')
    help_author = types.InlineKeyboardButton(text='Помощь', callback_data='help_author')
    profile = types.InlineKeyboardButton(text="Профиль", callback_data='profile')
    kb.add(schedule, help_author, profile)
    bot.send_message(message.chat.id, "Привет! Ты находишься в главном меню бота для онлайн школы. company, v1.0", reply_markup=kb, parse_mode='HTML')


#@bot.callback_query_handler(func=lambda call:True)
#def callback_query(call):
    #if call.data = 'profile':
        #user_id = call.from_user.id
        #bot.send_message(call.chat.id, f'Профиль:')
        #bot.send_message(call.chat.id, f'Ваш id: {user_id}')
    
    

#админпанель
@bot.message_handler(commands=['admin'])
def adminpanel(message):
    user_id = message.from_user.id
    if user_id == admin:
        kb = types.InlineKeyboardMarkup(row_width=1)
        adminschedule = types.InlineKeyboardButton(text='Администрирование расписанием', callback_data='adminschedule')
        help_author = types.InlineKeyboardButton(text='Помощь', callback_data='help_author')
        profile = types.InlineKeyboardButton(text="Управление профилями", callback_data='editprofiles')
        kb.add(help_author, adminschedule, profile)
        bot.send_message(message.chat.id, "Добро пожаловать в админ панель!", reply_markup=kb, parse_mode='HTML')
    else:
        print("Пользователь", user_id, "попытался получить доступ к админпанели.")
        kb = types.InlineKeyboardMarkup(row_width=1)
        kb.add(backinline_types)
        bot.send_message(message.chat.id, "Отказано в доступе.", reply_markup=backinline, parse_mode='HTML')

        
bot.infinity_polling()

