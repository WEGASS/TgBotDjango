from django.conf import settings
import telebot
import time
from tg.models import *

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    profile, _ = Profile.objects.get_or_create(external_id=chat_id)
    UserData.objects.get_or_create(profile=profile)
    question_age = Questions.objects.get(title='Возраст').question_text
    message = bot.send_message(message.chat.id, question_age)
    bot.register_next_step_handler(message, get_age_and_save)


def get_age_and_save(message):
    chat_id = message.chat.id
    age = message.text
    age_error = BotHelpMessage.objects.get(title='Ошибка возраст').text
    if not age.isdigit():
        msg = bot.reply_to(message, age_error)
        bot.register_next_step_handler(msg, get_age_and_save)
        return
    user_data = UserData.objects.get(profile__external_id=chat_id)
    user_data.age = age
    user_data.save()
    question_birthplace = Questions.objects.get(title='Место рождения').question_text
    message = bot.send_message(chat_id, question_birthplace)
    bot.register_next_step_handler(message, get_birthplace_and_save)


def get_birthplace_and_save(message):
    chat_id = message.chat.id
    birthplace = message.text
    user_data = UserData.objects.get(profile__external_id=chat_id)
    user_data.birthplace = birthplace
    user_data.save()
    thanks = BotHelpMessage.objects.get(title='Спасибо').text
    bot.send_message(chat_id, thanks)


@bot.message_handler(content_types='text')
def send_help_message(message):
    chat_id = message.chat.id
    help_message = BotHelpMessage.objects.get(title='Начать заново').text
    bot.send_message(chat_id, help_message)


def start_bot():
    while True:
        try:
            print('Bot starting')
            bot.polling(none_stop=True)
        except telebot.apihelper.ApiException as e:
            print(e)
            time.sleep(10)
