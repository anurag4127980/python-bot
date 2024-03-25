import time
import json
import telebot

TOKEN = "TRON"
BOT_TOKEN = "6570624343:AAEhriMK-kgVVVOx0DV4qoAD0xTS4JVTJ4Q"

bot = telebot.TeleBot(BOT_TOKEN)

questions = [
    "Please enter the Date?",
    "Which Stock you Invested in?",
    "What is the Quantity?",
    "Was it Buy or Sale?",
    "Give me the rate?"
]
answers = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    answers[user_id] = {}
    bot.send_message(user_id, "Bot started. Type 'record' to begin recording.")


@bot.message_handler(func=lambda message: message.text.lower() == 'record')
def start_recording(message):
    user_id = message.chat.id
    answers[user_id] = {}
    bot.send_message(user_id, questions[0])


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    if user_id not in answers:
        bot.send_message(user_id, "Please start the bot by typing /start or 'record'.")
        return

    current_question_index = len(answers[user_id])
    if current_question_index < len(questions):
        answers[user_id][questions[current_question_index]] = message.text
        if current_question_index + 1 < len(questions):
            bot.send_message(user_id, questions[current_question_index + 1])
        else:
            bot.send_message(user_id, "Thank you for answering the questions!")
            # You can process the collected answers here or save them to a file/database
            print(answers[user_id])
            del answers[user_id]
    else:
        bot.send_message(user_id, "All questions have been answered. Thank you!")


if __name__ == '__main__':
    bot.polling(none_stop=True)
