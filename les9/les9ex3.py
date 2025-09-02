# Напишите программу, которая считывает текст из
# файла (в файле может быть больше одной строки) и выводит
# в новый файл самое часто встречаемое слово в каждой
# строке и число – счётчик количества повторений этого слова
# в строке.
# 1. Открываем файл с текстом для чтения
from collections import Counter

# Чтение исходного файла
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

results = []

for line in lines:
    words = line.strip().split()
    if not words:
        results.append("")
        continue

    counter = Counter(words)
    most_common_word, count = counter.most_common(1)[0]
    results.append(f"{most_common_word} {count}")

# Запись в новый файл
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for res in results:
        outfile.write(res + '\n')
