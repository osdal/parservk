import pandas as pd
import re

# Чтение файла CSV
df = pd.read_csv("data.csv")

# Регулярное выражение для извлечения слов, начинающихся с заглавной буквы и заканчивающихся на "ич"
word_pattern = re.compile(r'\b[A-ЯЁ][а-яё]* [A-ЯЁ][а-яё]* [А-ЯЁ][а-яё]*ич\b')

# Регулярное выражение для извлечения дат
date_pattern = re.compile(r'\b(?:\d{1,2}\.\d{1,2}\.\d{2,4}|\d{1,2}\.\d{1,2}\.\d{2})\b')

# Массив для хранения пар значений
pairs = []

# Извлечение триплетов слов и дат из каждой ячейки
for index, row in df.iterrows():
    text = str(row["text"])  # Преобразование в строку
    words = word_pattern.findall(text)
    dates = date_pattern.findall(text)
    for word in words:
        for date in dates:
            pairs.append((word, date))

# Запись пар значений в текстовый файл
if pairs:
    with open("pairs.txt", "w", encoding="utf-8") as file:
        for pair in pairs:
            file.write(f"{pair[0]}:{pair[1]}\n")
    print("Файл 'pairs.txt' успешно создан.")
else:
    print("Нет данных для записи в файл.")

# Открыть файл pairs.txt для чтения
with open("pairs.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Открыть новый файл для записи
with open("pairs_filtered.txt", "w", encoding="utf-8") as file:
    # Проверить каждую строку
    for line in lines:
        # Проверить, содержит ли строка числа 2022 или 2023
        if "2022" not in line and "2023" not in line:
            # Записать строку в новый файл, если числа 2022 или 2023 не найдены
            file.write(line)

print("Файл 'pairs_filtered.txt' успешно создан.")

# Открыть файл pairs.txt для чтения
with open("pairs.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Открыть новый файл для записи
with open("pairs_filtered.txt", "w", encoding="utf-8") as file:
    # Проверить каждую строку
    for line in lines:
        # Проверить, содержит ли строка числа 22, 23 или 24
        if "22" not in line and "23" not in line and "24" not in line:
            # Записать строку в новый файл, если числа 22, 23 или 24 не найдены
            file.write(line)

print("Файл 'pairs_filtered.txt' успешно создан.")

# Открыть файл pairs.txt для чтения
with open("pairs.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Создать множество для хранения уникальных строк
unique_lines = set()

# Регулярное выражение для поиска чисел больше 2013
number_pattern = re.compile(r'\b(20[2-9]\d|2[1-9]\d{2}|[3-9]\d{3})\b')

# Открыть новый файл для записи
with open("pairs_filtered.txt", "w", encoding="utf-8") as file:
    # Проверить каждую строку
    for line in lines:
        # Проверить, не содержит ли строка чисел больше 2013
        if not number_pattern.search(line):
            # Проверить, если строка уже есть в уникальных строках
            if line not in unique_lines:
                # Записать строку в множество уникальных строк
                unique_lines.add(line)
                # Записать строку в новый файл
                file.write(line)

print("Файл 'pairs_filtered.txt' успешно создан.")