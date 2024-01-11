import telebot
from info import*
from telebot import types

bot = telebot.TeleBot(token=took)

user_data = {}

questions = {
    0: {"text": ".هل انت طالب في إسطنبول", "function": "ask_student_status"},
    1: {"text": "ما هو اسمك الرباعي؟", "function": "ask_full_name"}
    # يمكنك إضافة المزيد من الأسئلة هنا
}

def ask_student_status(message):
    user_id = message.chat.id
    current_question = get_current_question_for_user(user_id)
    
    if current_question:
        keyboard = create_yes_no_keyboard_0()
        bot.send_message(message.chat.id, current_question["text"], reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "No more questions available.")
        
def ask_full_name(message):
    user_id = message.chat.id
    current_question = get_current_question_for_user(user_id)
    
    if current_question:
        bot.send_message(message.chat.id, current_question["text"])
    else:
        bot.send_message(message.chat.id, "No more questions available.")
       

def create_yes_no_keyboard_0():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("نعم", callback_data='yes'), InlineKeyboardButton("لا", callback_data='no'))
    return keyboard

def create_keyboard_for_question(question_number):
    if question_number == 0 and question_valid_0:  # First question
        return create_yes_no_keyboard_0()
    else:
        return None  # Handle other questions as needed
question_valid_0 = True

def create_questions_for_user(user_id):
    global user_data
    if user_id not in user_data:
        user_data[user_id] = {
            'questions': questions,
            'current_question': 0
        }
    return user_data[user_id]['questions']

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_data
    user_id = message.chat.id
    user_data = {}
    questions_for_user = create_questions_for_user(user_id)
    current_question_for_user = get_current_question_for_user(user_id)

    if current_question_for_user:
        ask_student_status(message)
    else:
        bot.send_message(user_id, "No questions available at the moment.")

        
def update_question_for_user(user_id, response):
    global user_data
    if user_id in user_data:
        current_question = user_data[user_id]['current_question']
        user_questions = user_data[user_id]['questions']
        
        if current_question < len(user_questions):
            if response == 'yes':  # تحقق من الاستجابة إذا كانت نعم
                user_data[user_id]['current_question'] == 1
            else:
                # تحتاج لمعالجة الحالة التي تختار فيها "لا" هنا
                pass

def get_current_question_for_user(user_id):
    global user_data
    if user_id in user_data:
        current_question = user_data[user_id]['current_question']
        user_questions = user_data[user_id]['questions']
        if current_question < len(user_questions):
            return user_questions[current_question]
    return None
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global user_data
    user_id = message.chat.id
    response = message.text.lower()
    update_question_for_user(user_id, response)
    current_question_for_user = get_current_question_for_user(user_id)

    if current_question_for_user:
        ask_student_status(message)
    else:
        bot.send_message(user_id, "No more questions. Thank you!")

bot.polling(none_stop=True)
