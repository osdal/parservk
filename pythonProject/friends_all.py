import pandas as pd
import vk_api

# Чтение данных из файла friends.csv
data = pd.read_csv('friends.csv')

# Создание сессии ВКонтакте
vk_session = vk_api.VkApi(token='3439c2983439c2983439c298af372e797e334393439c29851c41e311644bc350d290ea7')
vk = vk_session.get_api()

# Функция для получения списка друзей пользователя по его ID
def get_friends(user_id):
    try:
        response = vk.friends.get(user_id=user_id)
        return response['items']
    except vk_api.exceptions.ApiError:
        return []

# Добавление столбца 'friends' в DataFrame и получение списка друзей для каждого пользователя
data['friends'] = data['ID'].apply(get_friends)

# Запись данных обратно в файл friends.csv
data.to_csv('friends.csv', index=False)
