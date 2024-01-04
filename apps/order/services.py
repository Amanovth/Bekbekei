import telebot
from .models import TeleBot as bot_base

def teleorder(id, first_name, last_name, number, products):
    bot = telebot.TeleBot(bot_base.objects.first().bot_token)


    order_message = f"Новый заказ!\n\n№ {id}\n\n\n"

    for i in products:
        product = i.product
        count = i.count
        order_message += f'Tовар - {product}\nКол-во - {count}\n\n'

    order_message += f'---------------------\nФИО - {last_name} {first_name}\nТел. номер - {number}'

    bot.send_message(chat_id=bot_base.objects.first().chat_id , text=order_message)

def teleordercancel(id):
    bot = telebot.TeleBot(bot_base.objects.first().bot_token)

    order_message = f"Заказ под айди {id} отменён!"

    bot.send_message(chat_id=bot_base.objects.first().chat_id , text=order_message)