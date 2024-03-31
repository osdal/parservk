import pandas as pd

# Чтение данных из файла members.csv с явным указанием разделителя и удалением пустых значений в заголовках
data = pd.read_csv('members.csv', delimiter=';', skipinitialspace=True)

# Отбор нужных столбцов
selected_columns = data[['ID', 'link', 'name', 'surname']]

# Запись данных в новый файл friends.csv
selected_columns.to_csv('friends.csv', index=False)
