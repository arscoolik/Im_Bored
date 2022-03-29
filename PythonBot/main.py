import requests
from datetime import datetime
from random import randint
import telebot
from auth_data import token
from telebot import types
from dataclasses import dataclass
from pyqiwip2p import QiwiP2P
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import markups as nav
from db import Database
from aiogram import executor
import sqlite3
import datetime

db = Database("database.db") #database with tables for goods and users
p2p = QiwiP2P(auth_key="<Qiwi Auth Key>")


def telegram_bot(token):
    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Наличие товара📤")
        item2 = types.KeyboardButton("Инструкция📚")
        item3 = types.KeyboardButton("Поддержка🛟")
        item4 = types.KeyboardButton("Купить💰")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Хола, тебя приветствует бот для покупки подарочного кода на Нетфликс!😉", reply_markup = markup)
        


    @bot.message_handler(content_types = ["text"])
    def handle_command(message):
        if message.chat.type == "private":
            if message.text == "Купить💰":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton("Главное меню")
                item2 = types.KeyboardButton("3 месяца")
                item3 = types.KeyboardButton("4 месяца")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                bot.send_message(message.chat.id, "На сколько месяцев вы хотите приобрести подписку?", reply_markup = markup)



            elif message.text == "Поддержка🛟":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton("Главное меню")
                markup.add(item1)
                bot.send_message(message.chat.id, "Напиши @danyadjan", reply_markup = markup)

            elif message.text == "Инструкция📚":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton("Главное меню")
                markup.add(item1)
                bot.send_message(message.chat.id, "Почитайте: https://github.com/arscoolik/Im_Bored/blob/main/PythonBot/readme.md", reply_markup = markup)

            elif message.text == "Наличие товара📤":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton("Главное меню")
                markup.add(item1)
                bot.send_message(message.chat.id, f"В наличии: \n {db.get_75_length() - db.get_check_length75()} промокод(a; ов) на ~3 месяца (1000 рублей) \n {db.get_100_length() - db.get_check_length100()} промокод(a; ов) на ~4 месяца (1200 рублей)", reply_markup = markup)

            elif message.text ==  "Главное меню":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton("Наличие товара📤")
                item2 = types.KeyboardButton("Инструкция📚")
                item3 = types.KeyboardButton("Поддержка🛟")
                item4 = types.KeyboardButton("Купить💰")
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, "Главное меню", reply_markup = markup)

            elif message.text == "3 месяца":
                if db.get_check(message.from_user.id):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item2 = types.KeyboardButton("Главное меню")
                    item3 = types.KeyboardButton("Остановить покупку")
                    markup.add(item2, item3)
                    bot.send_message(message.chat.id, "Вы ещё не оплатили предыдущий товар. Остановите покупку/Подождите 15 минут/Оплатите товар",reply_markup=markup)
                elif db.get_75_length() - db.get_check_length75():
                    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    comment = str(message.from_user.id) + "_" + str(randint(1000, 9999))
                    bill = p2p.bill(amount = 1000, lifetime = 10, comment = comment)
                    db.add_check(message.from_user.id, bill.bill_id, 75, datetime.datetime.now())
                    item1 = types.KeyboardButton("Проверить оплату")
                    item2 = types.KeyboardButton("Главное меню")
                    markup.add(item1, item2)
                    bot.send_message(message.chat.id, f"Ссылка для оплаты(активна 10 минут): {bill.pay_url}", reply_markup = markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    bot.send_message(message.chat.id, "К сожалению, сейчас данного товара нет😔", reply_markup = markup)
                    item2 = types.KeyboardButton("Главное меню")
                    markup.add(item2)

            elif message.text == "4 месяца":
                if db.get_check(message.from_user.id) :
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item2 = types.KeyboardButton("Главное меню")
                    item3 = types.KeyboardButton("Остановить покупку")
                    markup.add(item2, item3)
                    bot.send_message(message.chat.id, "Вы ещё не оплатили предыдущий товар. Остановите покупку/Подождите 15 минут/Оплатите товар", reply_markup=markup)

                elif db.get_100_length()-db.get_check_length100():
                    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    comment = str(message.from_user.id) + "_" + str(randint(1000, 9999))
                    bill = p2p.bill(amount = 1200, lifetime = 10, comment = comment)
                    db.add_check(message.from_user.id, bill.bill_id, 100, datetime.datetime.now())
                    item1 = types.KeyboardButton("Проверить оплату")
                    item2 = types.KeyboardButton("Главное меню")
                    markup.add(item1, item2)
                    bot.send_message(message.chat.id, f"Ссылка для оплаты(активна 10 минут): {bill.pay_url}", reply_markup = markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    bot.send_message(message.chat.id, "К сожалению, сейчас данного товара нет😔", reply_markup = markup)
                    item2 = types.KeyboardButton("Главное меню")
                    markup.add(item2)

            elif message.text == "Проверить оплату":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                info = db.get_check(message.from_user.id)
                if info != False:
                    if str(p2p.check(bill_id=info[0]).status) == "PAID":
                        db.delete(message.from_user.id)
                        if info[1] == 75:
                            bot.send_message(message.chat.id, f"Оплата прошла успешно, вот ваш код:", reply_markup = markup)
                            bot.send_message(message.chat.id, f"{db.get_code_75()}", reply_markup = markup)
                        elif info[1] == 100:
                            bot.send_message(message.chat.id, f"Оплата прошла успешно, вот ваш код:", reply_markup = markup)
                            bot.send_message(message.chat.id, f"{db.get_code_100()}", reply_markup = markup)
                    else:
                        bot.send_message(message.chat.id, f"Оплата ещё не прошла, пожалуйста подождите", reply_markup = markup)
                else:
                    print("error")

            elif message.text == "Остановить покупку":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Да")
                item2 = types.KeyboardButton("Нет")
                markup.add(item1, item2)
                bot.send_message(message.chat.id, f"Вы уверены?", reply_markup=markup)

            elif message.text == "Да":
                db.delete(message.from_user.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton("Главное меню")
                markup.add(item2)
                bot.send_message(message.chat.id, f"Вы приостановили покупку. Теперь вы можете оплатить другой товар", reply_markup=markup)

            elif message.text == "Нет":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton("Главное меню")
                markup.add(item2)
                bot.send_message(message.chat.id, f"Вернуться в главное меню", reply_markup=markup)
        last_mes = message.text
        check = db.get_check(message.from_user.id)
        if check:
            while True:
                if datetime.datetime.now() - datetime.timedelta(minutes=15, seconds = 0)>datetime.datetime.strptime((check[2].split('.'))[0], '%Y-%m-%d %H:%M:%S'):
                    db.delete(message.from_user.id)
                    if str(p2p.check(bill_id=check[0]).status) == "PAID":
                        if info[1] == 75:
                            bot.send_message(message.chat.id, f"Оплата прошла успешно, вот ваш код:", reply_markup=markup)
                            bot.send_message(message.chat.id, f"{db.get_code_75()}", reply_markup=markup)
                        elif info[1] == 100:
                            bot.send_message(message.chat.id, f"Оплата прошла успешно, вот ваш код:", reply_markup=markup)
                            bot.send_message(message.chat.id, f"{db.get_code_100()}", reply_markup=markup)
                    else:
                        bot.send_message(message.chat.id, f"Оплата не прошла", reply_markup=markup)
                        break
                if message.text != last_mes:
                    break

    bot.polling()





if __name__ == '__main__':
    # get_data()
    telegram_bot(token)