import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

# Dil terimlerini tanımla
languages = {
    "english": {
        "password_length": "Password Length:",
        "uppercase": "Uppercase Letters",
        "lowercase": "Lowercase Letters",
        "digits": "Digits",
        "special_chars": "Special Characters",
        "unique_chars": "Unique Characters",
        "generate_password": "Generate Password",
        "copy_password": "Copy Password",
        "language_select": "Language Select:",
        "language_options": ["English", "Mandarin Chinese"],
        "please_select_characters": "Please select character options!",
        "unique_password_error": "More characters needed to create a unique password!",
        "copied": "Copied!",
        "very_strong": "Very Strong",
        "strong": "Strong",
        "medium": "Medium",
        "weak": "Weak"
    },
    "mandarin_chinese": {
        "password_length": "密码长度：",
        "uppercase": "大写字母",
        "lowercase": "小写字母",
        "digits": "数字",
        "special_chars": "特殊字符",
        "unique_chars": "唯一字符",
        "generate_password": "生成密码",
        "copy_password": "复制密码",
        "language_select": "语言选择：",
        "language_options": ["English", "Mandarin Chinese"],
        "please_select_characters": "请选择字符选项！",
        "unique_password_error": "需要更多字符以创建唯一密码！",
        "copied": "已复制！",
        "very_strong": "非常强",
        "strong": "强",
        "medium": "中等",
        "weak": "弱"
    }
}

# Global değişkenler
current_language = "english"

# Dil seçimini değiştirme işlevi
def change_language(event):
    global current_language
    # ComboBox'tan gelen değeri doğru şekilde eşleştirecek mantığı ekleyin
    selected_language = language_selector.get().lower().replace(" ", "_")
    if selected_language in languages:
        current_language = selected_language
        # ComboBox ve diğer arayüz elemanlarını güncelleyin
        update_language()
        update_language_options()

# Dil seçeneklerini ComboBox'ta güncelleme işlevi
def update_language_options():
    # Dil seçeneklerini güncelleyin
    language_selector['values'] = languages[current_language]["language_options"]
    # Varsayılan olarak ilk seçeneği ayarlayın
    language_selector.current(0)

# Arayüz metinlerini güncelleme işlevi
def update_language():
    language_label.config(text=languages[current_language]["language_select"])
    length_label.config(text=languages[current_language]["password_length"])
    uppercase_check.config(text=languages[current_language]["uppercase"])
    lowercase_check.config(text=languages[current_language]["lowercase"])
    digits_check.config(text=languages[current_language]["digits"])
    special_chars_check.config(text=languages[current_language]["special_chars"])
    unique_chars_check.config(text=languages[current_language]["unique_chars"])
    generate_button.config(text=languages[current_language]["generate_password"])
    copy_button.config(text=languages[current_language]["copy_password"])
    strength_label.config(text="")
    password_display.config(text="")

# Şifre oluşturma işlevi
def generate_password():
    length_text = length_entry.get()
    if not length_text:
        password_display.config(text=languages[current_language]["please_select_characters"])
        return
    
    length = int(length_text)
    if length <= 0:
        password_display.config(text=languages[current_language]["please_select_characters"])
        return

    characters = ""
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if special_chars_var.get():
        characters += string.punctuation

    if not characters:
        password_display.config(text=languages[current_language]["please_select_characters"])
        return

    if unique_chars_var.get():
        if length > len(characters):
            password_display.config(text=languages[current_language]["unique_password_error"])
            return
        password = ''.join(random.sample(characters, length))
    else:
        password = ''.join(random.choice(characters) for _ in range(length))

    password_display.config(text=password)
    evaluate_strength(password, length)

# Şifre güvenliğini değerlendirme işlevi
def evaluate_strength(password, length):
    strength = 0
    character_sets = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    for char_set in character_sets:
        if any(char in char_set for char in password):
            strength += 1
    if length >= 12:
        strength += 1

    if strength == 5:
        strength_label.config(text=languages[current_language]["very_strong"])
    elif strength >= 3:
        strength_label.config(text=languages[current_language]["strong"])
    elif strength >= 2:
        strength_label.config(text=languages[current_language]["medium"])
    else:
        strength_label.config(text=languages[current_language]["weak"])

# Şifreyi panoya kopyalama işlevi
def copy_password():
    pyperclip.copy(password_display.cget("text"))
    ttk.Label(main_frame, text=languages[current_language]["copied"], foreground="green").grid(column=0, row=11, columnspan=2)

# Pencereyi oluştur
root = tk.Tk()
root.title("Strong Password Generator")

# Ana çerçeve oluştur
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dil seçimini oluştur
language_label = ttk.Label(main_frame, text=languages[current_language]["language_select"])
language_label.grid(column=0, row=0, sticky=tk.W)
language_selector = ttk.Combobox(main_frame, values=languages[current_language]["language_options"], state="readonly")
language_selector.current(0)
language_selector.grid(column=1, row=0, sticky=tk.W)
language_selector.bind("<<ComboboxSelected>>", change_language)

# Şifre uzunluğu etiketi ve giriş alanı
length_label = ttk.Label(main_frame, text=languages[current_language]["password_length"])
length_label.grid(column=0, row=1, sticky=tk.W)
length_entry = ttk.Entry(main_frame)
length_entry.grid(column=1, row=1, sticky=tk.W)

# Şifre karakter seçenekleri
uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(main_frame, text=languages[current_language]["uppercase"], variable=uppercase_var)
uppercase_check.grid(column=0, row=2, sticky=tk.W)
lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(main_frame, text=languages[current_language]["lowercase"], variable=lowercase_var)
lowercase_check.grid(column=0, row=3, sticky=tk.W)
digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(main_frame, text=languages[current_language]["digits"], variable=digits_var)
digits_check.grid(column=0, row=4, sticky=tk.W)
special_chars_var = tk.BooleanVar()
special_chars_check = ttk.Checkbutton(main_frame, text=languages[current_language]["special_chars"], variable=special_chars_var)
special_chars_check.grid(column=0, row=5, sticky=tk.W)
unique_chars_var = tk.BooleanVar()
unique_chars_check = ttk.Checkbutton(main_frame, text=languages[current_language]["unique_chars"], variable=unique_chars_var)
unique_chars_check.grid(column=0, row=6, sticky=tk.W)

# Şifre oluşturma ve kopyalama düğmeleri
generate_button = ttk.Button(main_frame, text=languages[current_language]["generate_password"], command=generate_password)
generate_button.grid(column=0, row=7, columnspan=2, sticky=tk.W+tk.E)
copy_button = ttk.Button(main_frame, text=languages[current_language]["copy_password"], command=copy_password)
copy_button.grid(column=0, row=8, columnspan=2, sticky=tk.W+tk.E)

# Şifre gösterici
password_display = ttk.Label(main_frame, text="")
password_display.grid(column=0, row=9, columnspan=2, pady=5)

# Şifre güvenliği değerlendirme etiketi
strength_label = ttk.Label(main_frame, text="")
strength_label.grid(column=0, row=10, columnspan=2, pady=5)

# Pencereyi merkezle
root.eval('tk::PlaceWindow . center')

# GUI döngüsünü başlat
root.mainloop()
