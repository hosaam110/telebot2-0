questions = {
    0: {"text": ".هل انت طالب في إسطنبول", "function": "ask_student_status"},
    1: {"text": "الاسم الرباعي باللغة العربية.", "function": "ask_arabic_name"},
    2: {"text": "الاسم الرباعي بالغة الإنجليزية.", "function": "ask_english_name"},
    3: {"text": "تاريخ الميلاد.", "function": "ask_date_of_birth"},
    4: {"text": "الجنس.", "function": "ask_gender"},
    5: {"text": "رقم الهاتف التركي.", "function": "ask_turkish_phone"},
    6: {"text": "رقم الواتس اب.", "function": "ask_whatsapp_number"},
    7: {"text": "موقع السكن.", "function": "ask_residence_location"},
    8: {"text": "البريد الالكتروني.", "function": "ask_email"},
    9: {"text": "اسم الجامعة او المعهد (باللغة الإنجليزية).", "function": "ask_university"},
    10: {"text": "التخصص الجامعي باللغة الإنجليزية.", "function": "ask_major"},
    11: {"text": "المرحلة الجامعية.", "function": "ask_academic_level"},
    12: {"text": "ارفاق الاورنجي بلقسي بصيغة PDF او صورة واضحة.", "function": "ask_orange_belt"},
    13: {"text": "ارفاق الهوية بصيغة PDF او صورة واضحة من الجهة الامامية.", "function": "ask_id_front"},
    14: {"text": "ارفاق الهوية بصيغة PDF او صورة واضحة من الجهة الخلفية.", "function": "ask_id_back"},
    15: {"text": "هل تقر بأن البيانات أعلاه صحيحة وتتعهد بتحديثها عند تغييرها أو عند الطلب وبناء عليه تطلب الموافقة على طلب العضوية في اتحاد الطلاب اليمنيين في تركيا وفقاً لأحكام العضوية الواردة في الباب الثاني من النظام الأساسي للاتحاد؟.", "function": "ask_confirmation"}
}



questions_to_edit = [
    {"text": "هل انت طالب في إسطنبول؟", "callback_data": "edit_question_0"},
    {"text": "الاسم الرباعي باللغة العربية.", "callback_data": "edit_question_1"},
    {"text": "الاسم الرباعي بالغة الإنجليزية.", "callback_data": "edit_question_2"},
    {"text": "تاريخ الميلاد.", "function": "edit_question_3"},
    {"text": "الجنس.", "function": "edit_question_4"},
    {"text": "رقم الهاتف التركي.", "function": "edit_question_5"},
    {"text": "رقم الواتس اب.", "function": "edit_question_6"},
    {"text": "موقع السكن.", "function": "edit_question_7"},
    {"text": "البريد الالكتروني.", "function": "edit_question_8"},
    {"text": "اسم الجامعة او المعهد (باللغة الإنجليزية).", "function": "edit_question_9"},
    {"text": "التخصص الجامعي باللغة الإنجليزية.", "function": "edit_question_10"},
    {"text": "المرحلة الجامعية.", "function": "edit_question_11"},
    {"text": "ارفاق الاورنجي بلقسي بصيغة PDF او صورة واضحة.", "function": "edit_question_12"},
    {"text": "ارفاق الهوية بصيغة PDF او صورة واضحة من الجهة الامامية.", "function": "edit_question_13"},
    {"text": "ارفاق الهوية بصيغة PDF او صورة واضحة من الجهة الخلفية.", "function": "edit_question_14"},
    {"text": "هل تقر بأن البيانات أعلاه صحيحة وتتعهد بتحديثها عند تغييرها أو عند الطلب وبناء عليه تطلب الموافقة على طلب العضوية في اتحاد الطلاب اليمنيين في تركيا وفقاً لأحكام العضوية الواردة في الباب الثاني من النظام الأساسي للاتحاد؟.", "function": "edit_question_15"}

]
