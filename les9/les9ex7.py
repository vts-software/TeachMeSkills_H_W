# 1. Спрашиваем имя файла, который будем шифровать
filename = input("Введите имя файла для шифрования: ")

# 2. Открываем файл и читаем все строки
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 3. Функция для шифра Цезаря
def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():  # Только буквы шифруем
            # Определяем, заглавная буква или маленькая
            start = ord('A') if ch.isupper() else ord('a')
            # Смещаем букву на shift и оборачиваем в пределах алфавита
            new_ch = chr((ord(ch) - start + shift) % 26 + start)
            result += new_ch
        else:
            # Если это не буква (пробел, цифра, знак) — не меняем
            result += ch
    return result

# 4. Шифруем каждую строку, увеличивая сдвиг
encrypted_lines = []
for i, line in enumerate(lines, start=1):  # i — номер строки (1, 2, 3...)
    encrypted_lines.append(caesar_cipher(line.strip(), i))

# 5. Показываем результат
print("\n=== Зашифрованный текст ===")
for enc in encrypted_lines:
    print(enc)
