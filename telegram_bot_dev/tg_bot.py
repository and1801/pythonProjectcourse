import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7780464626:AAEl5GZUEZlJuwu2MbQ095iJv23McMWFMzo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет, я чат-бот, который будет напоминать пить водичку и делать перерывы. Введите /help для списка доступных команд.')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать список доступных команд\n"
        "/time - Узнать текущее время\n"
        "/fact - Получить интересный факт о воде\n"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['time'])
def time_message(message):
    now = datetime.datetime.now().strftime('%H:%M')
    bot.reply_to(message, f'Текущее время: {now}')

@bot.message_handler(commands=['fact'])
def fact_message(message):
    facts = [
        'Вода составляет около 60% массы тела взрослого человека.',
        'В среднем человеку нужно пить около 2 литров воды в день.',
        'Вода помогает поддерживать температуру тела и смазывать суставы.',
        'Вода необходима для всех жизненно важных процессов в организме.',
        'Около 71% поверхности Земли покрыто водой.'
    ]
    random_fact = random.choice(facts)
    bot.reply_to(message, f'Вот интересный факт о воде: {random_fact}')

def send_reminders(chat_id):
    water_reminder_times = ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']
    break_reminder_interval = 60  # Minutes
    last_break_reminder = datetime.datetime.now()

    while True:
        now = datetime.datetime.now()
        current_time_str = now.strftime('%H:%M')

        # Напоминание о воде
        if current_time_str in water_reminder_times:
            bot.send_message(chat_id, 'Напоминание: выпейте воды!')
            time.sleep(61)

        # Напоминание о разминке
        if (now - last_break_reminder).total_seconds() >= break_reminder_interval * 60:
            bot.send_message(chat_id, 'Напоминание: время размяться и отдохнуть от компьютера!')
            last_break_reminder = now

        time.sleep(1)

bot.polling(none_stop=True)