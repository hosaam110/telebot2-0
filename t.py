from info import *
from check import *
from Google import *
from googleapiclient.http import MediaFileUpload
from collections import defaultdict


bot = telebot.TeleBot(token=took)
user_data = {}
current_question = 0
questions = {
    0: {"text": ".هل انت طالب في إسطنبول", "function": "ask_student_status"},
    1: {"text": "الاسم الرباعي باللغة العربية.", "function": "ask_arabic_name"},
    2: {"text": "الاسم الرباعي بالغة الإنجليزية.", "function": "ask_english_name"},
    3: {"text": "ارفاق الاورنجي بلقسي بصيغة PDF او صورة واضحة.", "function": "ask_orange_belt"},
    4: {"text": "ارفاق الهوية بصيغة PDF او صورة واضحة من الجهة الامامية.", "function": "ask_id_front"},
    5: {"text": "ارفاق الهوية بصيغة PDF او صورة واضحة من الجهة الخلفية.", "function": "ask_id_back"},
    6: {"text": "هل تقر بأن البيانات أعلاه صحيحة وتتعهد بتحديثها عند تغييرها أو عند الطلب وبناء عليه تطلب الموافقة على طلب العضوية في اتحاد الطلاب اليمنيين في تركيا وفقاً لأحكام العضوية الواردة في الباب الثاني من النظام الأساسي للاتحاد؟.", "function": "ask_confirmation"}
}

def ask_student_status(original_message):
    keyboard = create_yes_no_keyboard_0()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)

def ask_arabic_name(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_english_name(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_orange_belt(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_id_front(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_id_back(original_message):
    bot.send_message(original_message.chat.id, questions[current_question]["text"])

def ask_student_status_6(original_message):
    keyboard = create_yes_no_keyboard_6()
    bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=keyboard)



def create_yes_no_keyboard_0(user_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("نعم", callback_data='yes'), InlineKeyboardButton("لا", callback_data='no'))
    return keyboard

def create_yes_no_keyboard_6(user_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("نعم", callback_data='yes'), InlineKeyboardButton("لا", callback_data='no'))
    return keyboard

user_data = defaultdict(dict)

@bot.message_handler(commands=['start'])
def start(original_message):
    global current_membership_number, user_data, current_question
    user_data = {}
    current_question = 0
    user_id = str(original_message.from_user.id)

    # تحديد user_id واستخدامه لتوليد رقم العضوية
    current_membership_number = generate_membership_number(user_id)
    user_data.setdefault(user_id, {})["membership_number"] = current_membership_number

    welcome_message = f"مرحبًا! أهلاً بك في استبياننا. رقم عضويتك المؤقت هو: {current_membership_number}"
    start_button = InlineKeyboardMarkup()
    start_button.add(InlineKeyboardButton("بدء الاستبيان", callback_data='start_questionnaire'))

    bot.send_message(original_message.chat.id, welcome_message, reply_markup=start_button)

question_valid_0 = True
question_valid_6 = True
current_question = 0
user_data = {}

last_answer = None
is_yes_clicked_0 = False
is_no_clicked_0 = False
is_yes_clicked_6 = False
is_no_clicked_6 = False

def create_keyboard_for_question(user_id, question_number):
    # تحقق مما إذا كانت الإجابة على السؤال الحالي موجودة في user_data
    if user_id in user_data and question_number in user_data[user_id]:
        return None  # لقد تم الرد على هذا السؤال من قبل
    else:
        # يمكنك هنا إنشاء لوحة المفاتيح الخاصة بالسؤال
        if question_number == 0:
            return create_yes_no_keyboard_0(user_id)
        elif question_number == 6:
            return create_yes_no_keyboard_6(user_id)
        else:
            return None  # تحديد ما إذا كان هناك لوحة مفاتيح للسؤال الآخر

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    global current_question, user_data, is_yes_clicked_0, is_no_clicked_0, is_yes_clicked_6, is_no_clicked_6
    
    # إرسال أول سؤال عند الضغط على بدء الاستبيان
    if call.data == 'start_questionnaire':
        user_id = str(call.from_user.id)
        user_data[user_id] = {}  # إعداد بيانات المستخدم الجديدة
        user_input = call.data
        user_data[current_question] = user_input
        current_question = 0  # الانتقال إلى سؤال رقم 0
        is_yes_clicked_0 = False
        is_no_clicked_0 = False
        is_yes_clicked_6 = False
        is_no_clicked_6 = False
        # إرسال رقم العضوية المؤقتة للمستخدم
        bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(user_id, current_question))
        return

    if call.data == 'yes' and question_valid_0 and current_question < len(questions) and not is_yes_clicked_0 and not is_no_clicked_0:
        user_input = call.data
        user_data[current_question] = user_input
        is_yes_clicked_0 = True
        is_no_clicked_0 = False  # تأكد من إعادة تعيين حالة الزر الآخر

        current_question = 1
        user_id = str(call.from_user.id)  # تعيين user_id هنا
        bot.send_message(call.message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(user_id, current_question))
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
    
    if call.data == 'yes' and question_valid_6 and current_question == 6 and not is_yes_clicked_6 and not is_no_clicked_6:
        user_input = call.data
        user_data[current_question] = user_input
        is_yes_clicked_6 = True
        is_no_clicked_6 = False  # تعطيل الزر 'no'
        
        user_id = str(call.from_user.id)  # تعيين user_id هنا
        # إذا كان السؤال هو الأخير والإجابة "نعم"، حفظ البيانات
        save_data(call.message)  # حفظ البيانات بعد الضغط على "نعم" في سؤال 15
        return
    else:
        if call.data == 'no' and question_valid_6 and current_question < len(questions) and not is_no_clicked_6 and not is_yes_clicked_6:
            user_input = call.data
            user_data[current_question] = user_input
            is_no_clicked_6 = True
            is_yes_clicked_6 = False  # تعطيل الزر 'yes'
            apology_message = "يرجى التحقق من معلوماتك والمحاولة لاحقا"
            bot.send_message(call.message.chat.id, apology_message)
            current_question = 0  # الانتهاء من الاستبيان
            user_data = {}  # إعادة تهيئة البيانات للسؤال الأول
            return

@bot.message_handler(func=lambda message: True, content_types=['document', 'photo', 'text'])
def handle_messages(original_message):
    global current_question, user_data, current_membership_number
    

    user_input = original_message.text
    user_id = str(original_message.from_user.id)  # الحصول على معرّف المستخدم
    # التحقق من معرَّف المستخدم وتخزين البيانات بناءً على ذلك
    if user_id not in user_data:
        user_data[user_id] = {}  # إعداد بيانات المستخدم الجديدة

    # Handling questions
    if current_question == 0:
        if original_message.content_type != 'text':
            bot.send_message(original_message.chat.id, "يرجى اختيار الخيارات المتاحة.")
            return
    elif current_question == 6:
        if original_message.content_type != 'text':
            bot.send_message(original_message.chat.id, "يرجى اختيار الخيارات المتاحة.")
            return
    elif current_question == 1:
        if not check_arabic_name(user_input):
            bot.send_message(original_message.chat.id, "الرجاء إدخال اسم عربي صحيح مكون من أربعة أسماء.")
            return
        user_data[user_id][current_question] = user_input  # حفظ البيانات لمستخدم معين
    elif current_question == 2:
        if not check_english_name(user_input):
            bot.send_message(original_message.chat.id, "الرجاء إدخال اسم إنجليزي صحيح مكون من أربعة أسماء.")
            return
        user_data[user_id][current_question] = user_input  # حفظ البيانات لمستخدم معين
    elif current_question in [3, 4, 5]:
        user_id = str(original_message.from_user.id)
        user_info = user_data.get(user_id, {})  # الحصول على بيانات المستخدم باستخدام معرَّفه

        current_membership_number = user_info.get("membership_number")  # الحصول على رقم العضوية من بيانات المستخدم
        user_id = str(original_message.from_user.id)
        user_info = user_data.get(user_id, {})  # الحصول على بيانات المستخدم باستخدام معرَّفه
        if original_message.content_type == 'document' and original_message.document.mime_type == 'application/pdf':
            save_file_to_drive(original_message, current_question)
        elif original_message.content_type == 'photo' and original_message.photo[0].file_size < 5242880:
            save_file_to_drive(original_message, current_question)
        else:
            bot.send_message(original_message.chat.id, "الرجاء إرسال ملف PDF أو صورة JPG صالحة.")
            return

    current_question += 1

    # إذا كان هناك أسئلة أخرى لم يتم الرد عليها بعد، استمر في طرح الأسئلة
    if current_question < len(questions):
        bot.send_message(original_message.chat.id, questions[current_question]["text"], reply_markup=create_keyboard_for_question(user_id, current_question))
    else:
        save_data(original_message)  # حفظ البيانات بعد الانتهاء من الاستبيان
        current_question = 0
        
import random
import string

def generate_membership_number(user_id):
    # إنشاء رقم عشوائي للعضوية
    allowed_characters = string.ascii_letters + string.digits
    membership_length = 8

    if user_id:
        user_id = user_id.replace('_', '')  # إزالة الشرطات الموجودة في user_id إذا وجدت
        membership_number = f"{user_id}_{random.randint(100, 999)}_{''.join(random.choices(allowed_characters, k=membership_length))}"
    else:
        membership_number = ''.join(random.choices(allowed_characters, k=membership_length))

    return membership_number

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
    global current_membership_number, user_data, current_question
    chat_id = original_message.chat.id
    user_id = str(original_message.from_user.id)

    # جمع البيانات التي ترغب في حفظها
    data_to_save = [
        user_data[user_id].get("membership_number", 'N/A'),  # Use the membership_number here
        user_data[user_id].get(1, 'N/A'),  # بيانات الاسم العربي
        user_data[user_id].get(2, 'N/A'),  # بيانات الاسم العربي
        user_data[user_id].get(3, 'N/A'),  # بيانات الاسم العربي
        user_data[user_id].get(4, 'N/A'),  # بيانات الاسم العربي
        user_data[user_id].get(5, 'N/A'),  # بيانات الاسم العربي
        user_data[user_id].get(6, 'N/A')  # بيانات الاسم العربي
    ]

    # استدعاء دالة حفظ البيانات في ورقة البيانات
    success, error_message = save_to_google_sheet(data_to_save)
    if success:
        bot.send_message(original_message.chat.id, f"تم حفظ البيانات برقم العضوية: {user_data[user_id].get('membership_number')}")
    else:
        bot.send_message(original_message, f"حدث خطأ أثناء محاولة حفظ البيانات في ورقة البيانات: {error_message}")

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
    current_membership_number = user_data.get("membership_number")
    user_id = str(message.from_user.id)



    if current_membership_number:
        if current_question == 3:
            file_name = f"orange_belt_{current_membership_number}.pdf" if message.document else f"orange_belt_{current_membership_number}.jpg"
        elif current_question == 4:
            file_name = f"id_front_{current_membership_number}.pdf" if message.document else f"id_front_{current_membership_number}.jpg"
        elif current_question == 5:
            file_name = f"id_back_{current_membership_number}.pdf" if message.document else f"id_back_{current_membership_number}.jpg"

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
