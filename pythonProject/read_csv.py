import pandas as pd
import re

# # Чтение файла CSV
df = pd.read_csv("group_posts.csv")

# Создание регулярного выражения для поиска дат
date_pattern = re.compile(r'\b(?:\d{1,2}\.\d{1,2}\.\d{2,4}|\d{1,2}\.\d{1,2}\.\d{2})\b')
# Регулярное выражение для поиска ключевых слов
keyword_pattern = re.compile(r'г\.?\s?р\.?|рожд')

# # Массив для хранения строк с найденными датами
found_rows = []

# Поиск дат в каждой строке столбца "text"
for index, row in df.iterrows():
    text = str(row["text"])  # Преобразование в строку
    matches = date_pattern.search(text)
    if matches:
        found_rows.append(row["text"])

# Создание нового DataFrame на основе найденных строк
found_df = pd.DataFrame(found_rows)

# Сохранение в файл CSV
found_df.to_csv("data.csv", index=False)
