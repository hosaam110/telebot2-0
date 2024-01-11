from info import *
from questions import *
from check import *
from Google import *
from googleapiclient.http import MediaFileUpload

bot = telebot.TeleBot(token=took)
current_membership_number = None

user_data = {}
current_question = 0

def ask_student_status(original_message):
    keyboard = create_yes_no_keyboard_0()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)

def ask_arabic_name(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_english_name(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_date_of_birth(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_gender(original_message):
    keyboard = create_gender_keyboard()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)

def ask_turkish_phone(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_whatsapp_number(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_residence_location(original_message):
    keyboard = create_residence_location_keyboard()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)

def ask_email(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_university(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_major(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_academic_level(original_message):
    keyboard = create_academic_level_keyboard()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)

def ask_orange_belt(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_id_front(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_id_back(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])
    
def ask_student_status(original_message):
    keyboard = create_yes_no_keyboard_15()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)


def create_yes_no_keyboard_0():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("نعم", callback_data='yes'), InlineKeyboardButton("لا", callback_data='no'))
    return keyboard

# دالة إنشاء لوحة مفاتيح بزرين نعم ولا
def create_yes_no_keyboard_15():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("نعم", callback_data='yes'), InlineKeyboardButton("لا", callback_data='no'))
    return keyboard

# دالة إنشاء لوحة مفاتيح الجنس
def create_gender_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("ذكر", callback_data='male'), InlineKeyboardButton("انثى", callback_data='female'))
    return keyboard

# دالة إنشاء لوحة مفاتيح موقع السكن
def create_residence_location_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("الجزء الأوربي", callback_data='european_part'), InlineKeyboardButton("الجزء الاسيوي", callback_data='asian_part'))
    return keyboard

# دالة إنشاء لوحة مفاتيح المرحلة الجامعية
def create_academic_level_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("تحضيري", callback_data='preparatory'),
        InlineKeyboardButton("مستوى اول", callback_data='level_1'),
        InlineKeyboardButton("مستوى ثاني", callback_data='level_2'),
        InlineKeyboardButton("مستوى ثالث", callback_data='level_3'),
        InlineKeyboardButton("مستوى رابع", callback_data='level_4'),
        InlineKeyboardButton("مستوى خامس", callback_data='level_5'),
        InlineKeyboardButton("سنة الامتياز", callback_data='internship_year'),
        InlineKeyboardButton("ماجستير", callback_data='master'),
        InlineKeyboardButton("دكتوراه", callback_data='phd'),
        InlineKeyboardButton("ما بعد الدكتوراه", callback_data='post_phd')
    )
    return keyboard
    
@bot.message_handler(commands=['start'])
def start(original_message):
    global current_question, user_data, membership_number
    user_data = {}
    current_question = 0

    # الرسالة الترحيبية
    welcome_message = "مرحباً! أهلاً بك في استبياننا يرجى الضغط على الزر أدناه للبدء في الأسئلة." 
    
    # زر البدء بالأسئلة
    start_button = InlineKeyboardMarkup()
    start_button.add(InlineKeyboardButton("بدء الاستبيان", callback_data='start_questionnaire'))

    # إرسال الرسالة الترحيبية مع الزر لبدء الأسئلة
    bot.send_message(original_message.chat.id, welcome_message, reply_markup=start_button)

def create_keyboard_for_question(question_number):
    if question_number == 0 and question_valid_0:  # First question
        return create_yes_no_keyboard_0()
    elif question_number == 4 and question_valid_4:  # Fourth question
        return create_gender_keyboard()
    elif question_number == 7 and question_valid_7:  # Seventh question
        return create_residence_location_keyboard()
    elif question_number == 11 and question_valid_11:  # Eleventh question
        return create_academic_level_keyboard()
    elif question_number == 15 and question_valid_15:  # Last question
        return create_yes_no_keyboard_15()
    else:
        return None  # Handle other questions as needed

# تعريف المتغيرات لتتبع صحة الخيارات في كل سؤال
question_valid_0 = True
question_valid_4 = True
question_valid_7 = True
question_valid_11 = True
question_valid_15 = True

current_question = 0
user_data = {}

last_answer = None

is_yes_clicked_0 = False
is_no_clicked_0 = False
is_yes_clicked_15 = False
is_no_clicked_15 = False
is_male_clicked = False
is_female_clicked = False
is_european_part_clicked = False
is_asian_part_clicked = False
academic_level_clicked = {
    'preparatory': False,
    'level_1': False,
    'level_2': False,
    'level_3': False,
    'level_4': False,
    'level_5': False,
    'internship_year': False,
    'master': False,
    'phd': False,
    'post_phd': False
}

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    global current_question, user_data, is_yes_clicked_0, is_no_clicked_0,is_yes_clicked_15, is_no_clicked_15, is_male_clicked, is_female_clicked, is_european_part_clicked, is_asian_part_clicked, academic_level_clicked

    # إرسال أول سؤال عند الضغط على بدء الاستبيان
    if call.data == 'start_questionnaire':
        user_input = call.data
        user_data[current_question] = user_input
        current_question = 0  # الانتقال إلى سؤال رقم 0
        is_yes_clicked_0 = False
        is_no_clicked_0 = False
        is_male_clicked = False
        is_female_clicked = False
        is_european_part_clicked = False
        is_asian_part_clicked = False
        academic_level_clicked = {
            'preparatory': False,
            'level_1': False,
            'level_2': False,
            'level_3': False,
            'level_4': False,
            'level_5': False,
            'internship_year': False,
            'master': False,
            'phd': False,
            'post_phd': False
        }
        is_yes_clicked_15 = False
        is_no_clicked_15 = False
        bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
        return
    
    if call.data == 'yes' and question_valid_0 and current_question < len(questions) and not is_yes_clicked_0 and not is_no_clicked_0:
        user_input = call.data
        user_data[current_question] = user_input
        is_yes_clicked_0 = True
        is_no_clicked_0 = False  # تأكد من إعادة تعيين حالة الزر الآخر

        current_question = 1
        bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
        return

    elif call.data == 'no' and question_valid_0 and current_question < len(questions) and not is_no_clicked_0 and not is_yes_clicked_0:
        user_input = call.data
        user_data[current_question] = user_input
        is_no_clicked_0 = True
        is_yes_clicked_0 = False  # تأكد من إعادة تعيين حالة الزر الآخر

        apology_message = "We apologize, the membership is currently for Istanbul students only. Thank you!"
        bot.send_message(call.message.chat.id, text=apology_message)

        current_question = 0  # الانتهاء من الاستبيان
        user_data = {}  # إعادة تهيئة البيانات للسؤال الأول
        return
    elif (call.data == 'male' or call.data == 'female') and question_valid_4 and current_question == 4:
        user_input = call.data
        user_data[current_question] = user_input

        if call.data == 'male' and not is_female_clicked:  # إذا تم اختيار "ذكر" ولم يتم اختيار "أنثى"
            current_question = 5  # الانتقال إلى سؤال رقم 5
            is_male_clicked = True
            is_female_clicked = False
            bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
            return
        elif call.data == 'female' and not is_male_clicked:  # إذا تم اختيار "أنثى" ولم يتم اختيار "ذكر"
            current_question = 5  # الانتقال إلى سؤال رقم 5
            is_female_clicked = True
            is_male_clicked = False
            bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
            return
        
    elif (call.data == 'european_part' or call.data == 'asian_part') and question_valid_7 and current_question == 7:
        user_input = call.data
        user_data[current_question] = user_input

        if call.data == 'european_part' and not is_asian_part_clicked:
            is_european_part_clicked = True
            is_asian_part_clicked = False
            current_question = 8
            bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
            return
        elif call.data == 'asian_part' and not is_european_part_clicked:
            is_asian_part_clicked = True
            is_european_part_clicked = False
            current_question = 8
            bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
            return
        
    elif (call.data in academic_level_clicked) and question_valid_11 and current_question == 11:
        user_input = call.data
        user_data[current_question] = user_input

        if not academic_level_clicked[call.data]:
            academic_level_clicked[call.data] = True
            current_question = 12
            bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
            return
    
    if call.data == 'yes' and question_valid_15 and current_question == 15 and not is_yes_clicked_15 and not is_no_clicked_15:
        user_input = call.data
        user_data[current_question] = user_input
        is_yes_clicked_15 = True
        is_no_clicked_15 = False  # تعطيل الزر 'no'

        # إذا كان السؤال هو الأخير والإجابة "نعم"، حفظ البيانات
        save_data(call.message)  # حفظ البيانات بعد الضغط على "نعم" في سؤال 15
        return
    else:
        if call.data == 'no' and question_valid_15 and current_question < len(questions) and not is_no_clicked_15 and not is_yes_clicked_15:
            user_input = call.data
            user_data[current_question] = user_input
            is_no_clicked_15 = True
            is_yes_clicked_15 = False  # تعطيل الزر 'yes'
            apology_message = "يرجى التحقق من معلوماتك والمحاولة لاحقا"
            bot.send_message(call.message.chat.id, apology_message)
            current_question = 0  # الانتهاء من الاستبيان
            user_data = {}  # إعادة تهيئة البيانات للسؤال الأول
            return
        
@bot.message_handler(func=lambda message: True,content_types=['document', 'photo', 'text'])
def handle_messages(original_message):
    global current_question, user_data, membership_counter

    # Save user response
    user_input = original_message.text

        # Handling questions 0, 4, 7, 11, 15
    if current_question in [0, 4, 7, 11, 15]:
        if original_message.content_type == 'text':
            bot.send_message(original_message.chat.id, "يرجى الاختيار من الخيارات المتاحة.")
            return
    # elif current_question == 1:
    #     # Validate Arabic name
    #     if not check_arabic_name(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال اسم عربي صحيح مكون من أربعة أسماء.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 2:
    #     # Validate English name
    #     if not check_english_name(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال اسم إنجليزي صحيح مكون من أربعة أسماء.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 3:
    #     # Validate date of birth
    #     if not validate_date(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال تاريخ الميلاد بالصيغة الصحيحة YYYY-MM-DD.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 5:
    #     # Validate Turkish phone number
    #     if not check_turkish_phone_number(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال رقم هاتف تركي صحيح مكون من أرقام فقط ويبدأ بـ 05.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 6:
    #     # Validate WhatsApp number
    #     if not check_whatsapp_number(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال رقم واتساب صحيح مكون من أرقام فقط ويبدأ بـ ...+ مع مفتاح الخط الدولي.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 8:
    #     # Validate email
    #     if not check_email(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال بريد إلكتروني صحيح.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 9:
    #     # Validate English university/institution name
    #     if not check_university_english_name(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال اسم الجامعة بالإنجليزي.")
    #         return
    #     user_data[current_question] = user_input
    # elif current_question == 10:
    #     # Validate English major name
    #     if not check_major_english_name(user_input):
    #         bot.send_message(original_message.chat.id, "الرجاء إدخال اسم الجامعة بالإنجليزي.")
    #         return
    #     user_data[current_question] = user_input

    elif current_question in [12, 13, 14]:
        if original_message.content_type == 'document' and original_message.document.mime_type == 'application/pdf':
            save_file_to_drive(original_message, current_question)

        elif original_message.content_type == 'photo' and original_message.photo[0].file_size < 5242880:
            save_file_to_drive(original_message, current_question)
        else:
            bot.send_message(original_message.chat.id, "يرجى إرسال ملف PDF أو صورة JPG صالحة.")
            return  # Do not increase current_question
        
    current_question += 1

    if current_question < len(questions):
        bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(current_question))
    else:
        save_data(original_message)  # استدعاء دالة حفظ البيانات بعد جمعها من المستخدم

        # Reset values for the next survey
        current_question = 0
        user_data = {}

# تعريف نطاق الوصول
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# اسم ملف الاعتماد
creds = ServiceAccountCredentials.from_json_keyfile_name('sunlit-realm-311015-2cbfedf98184.json', scope)

# اتصال بواجهة برمجة التطبيقات
client = gspread.authorize(creds)

# معرّف ورقة البيانات
spreadsheet_id = '1P9GwlGiOg9ya04Nr4Gek9JjQ__SAhmjqanXicWAZ2Hg'

# دالة لحفظ البيانات في ورقة البيانات
def save_to_google_sheet(data):
    try:
        # فتح ورقة البيانات باستخدام معرّفها
        sheet = client.open_by_key(spreadsheet_id).sheet1
        
        # إضافة بيانات جديدة إلى الورقة
        sheet.append_row(data)
        
        return True, "تم حفظ البيانات بنجاح في Google Spreadsheet."
    except Exception as e:
        return False, f"حدث خطأ أثناء محاولة حفظ البيانات في Google Spreadsheet: {str(e)}"

# الدالة لحفظ البيانات بعد جمعها من المستخدم
def save_data(original_message):
    chat_id = original_message.chat.id
    user_data = {}
    current_question = 0


    # جمع البيانات التي ترغب في حفظها
    data_to_save = [
        generate_membership_number(chat_id),
        user_data.get(1, 'N/A'),  # بيانات الاسم العربي
        user_data.get(2, 'N/A'),  # بيانات الاسم الإنجليزي
        user_data.get(3, 'N/A'),  # بيانات تاريخ الميلاد
        user_data.get(4, 'N/A'),  # بيانات الجنس
        user_data.get(5, 'N/A'),  # بيانات رقم الهاتف التركي
        user_data.get(6, 'N/A'),  # بيانات رقم واتساب
        user_data.get(7, 'N/A'),  # بيانات موقع السكن
        user_data.get(8, 'N/A'),  # بيانات البريد الإلكتروني
        user_data.get(9, 'N/A'),  # بيانات الجامعة
        user_data.get(10, 'N/A'),  # بيانات التخصص
        user_data.get(11, 'N/A'),  # بيانات المرحلة الأكاديمية
        user_data.get(12, 'N/A'),  # بيانات حزام البرتقالي
        user_data.get(13, 'N/A'),  # بيانات الهوية الأمامية
        user_data.get(14, 'N/A'),  # بيانات الهوية الخلفية
        user_data.get(15, 'N/A')  # بيانات التأكيد
    ]
    
    # استدعاء دالة حفظ البيانات في ورقة البيانات
    success, error_message = save_to_google_sheet(data_to_save)
    if success:
        bot.send_message(original_message.chat.id, f"تم حفظ البيانات برقم العضوية: {data_to_save[0]}")
    else:
        bot.send_message(original_message, f"حدث خطأ أثناء محاولة حفظ البيانات في ورقة البيانات: {error_message}")# دالة توليد رقم عضوية متسلسل


import random
import string
from itertools import count

membership_counter = count(start=1, step=1)

def generate_membership_number(chat_id):
    global membership_counter
    # Use the same logic as before to generate the membership number
    serial_number = next(membership_counter)
    new_membership_number = f"{chat_id}_{serial_number:06d}"
    return new_membership_number

# تفاصيل المصادقة على حساب Google Drive الخاص بك
creds = service_account.Credentials.from_service_account_file('sunlit-realm-311015-2cbfedf98184.json')  # تعديل المسار إلى ملف JSON الخاص بك

# إنشاء اتصال مع Google Drive
service = build('drive', 'v3', credentials=creds)
# دالة الحفظ إلى Google Drive
def save_file_to_drive(message, current_question):
    global current_membership_number
    folder_id = '1wsAO8arRbzK_aVpCpNVVxSb1RRFhEnSD'
    file_id = message.document.file_id if message.document else message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

# طريقة الاستدعاء الصحيحة للدالة generate_membership_number()
    membership_number = generate_membership_number(message.chat.id)


    if membership_number:
        if current_question == 12:
            file_name = f"orange_belt_{membership_number}.pdf" if message.document else f"orange_belt_{membership_number}.jpg"
        elif current_question == 13:
            file_name = f"id_front_{membership_number}.pdf" if message.document else f"id_front_{membership_number}.jpg"
        elif current_question == 14:
            file_name = f"id_back_{membership_number}.pdf" if message.document else f"id_back_{membership_number}.jpg"

        # حفظ الملف المحمل مؤقتًا
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        # تحميل الملف إلى Google Drive
        media = MediaFileUpload(file_name, mimetype='application/pdf', resumable=True)
        file_metadata = {'name': file_name, 'parents': [folder_id]}
        service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        bot.reply_to(message, f"تم حفظ {file_name} في Google Drive بنجاح.")
    else:
        bot.reply_to(message, "حدثت مشكلة في توليد رقم العضوية. يرجى المحاولة مرة أخرى.")


bot.polling(none_stop=True)
