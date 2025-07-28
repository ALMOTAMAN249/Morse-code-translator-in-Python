# Morse code table (A-Z, 0-9)
morse_table = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',  # A-I
    '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',  # J-T
    '..-', '...-', '.--', '-..-', '-.--', '--..',  # U-Z
    '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.'  # 0-9
]

# حروف الأبجدية الإنجليزية
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# تحويل القائمة إلى Dictionary
morse_dict = {letters[i]: morse_table[i] for i in range(len(letters))}

# إدخال المستخدم
text = input("Type your text: ").upper()

# تحويل النص إلى مورس
morse_output = []

for char in text:
    if char in morse_dict:
        morse_output.append(morse_dict[char])
    elif char == ' ':
        morse_output.append('/')  # نستخدم / للفصل بين الكلمات
    else:
        morse_output.append('?')  # رموز غير معروفة

# عرض النتيجة
print('Morse Code:', ' '.join(morse_output))
