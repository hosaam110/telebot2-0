from info import *

def check_arabic_name(name):
    arabic_name_pattern = r'^[\u0621-\u064A]{2,}\s[\u0621-\u064A]{2,}\s[\u0621-\u064A]{2,}\s[\u0621-\u064A]{2,}$'

    if re.match(arabic_name_pattern, name):
        return True
    else:
        return False

def check_english_name(name):
    english_name_pattern = r'^[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+$'

    if re.match(english_name_pattern, name):
        return True
    else:
        return False
    
def validate_date(date_text):
    try:
        time.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def check_turkish_phone_number(phone_number):
    # يتحقق التعبير العادي من أن الرقم يحتوي على أرقام فقط ويبدأ بـ 90
    turkish_phone_pattern = r'^\+90[0-9]+$'

    if phone_number.startswith("05") and phone_number[3:].isdigit() and len(phone_number) == 11:
        return True
    else:
        return False

def check_whatsapp_number(whatsapp_number):
    if whatsapp_number.startswith("+") and whatsapp_number[1:].isdigit():
        return True
    else:
        return False
    
def check_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_pattern, email):
        return True
    else:
        return False
    
def check_university_english_name(name):
    english_name_pattern = r'^[a-zA-Z0-9\s]+$'

    if re.match(english_name_pattern, name):
        return True
    else:
        return False
    
def check_major_english_name(major_name):
    # Regular expression pattern for English major name
    english_major_pattern = r'^[a-zA-Z\s]+$'

    if re.match(english_major_pattern, major_name):
        return True
    else:
        return False

