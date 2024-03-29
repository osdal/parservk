import vk_api
import csv

# Функция для получения списка друзей пользователя по его айди
def get_friends(vk_session, user_id):
    try:
        response = vk_session.method('friends.get', {'user_id': user_id})
        if response and 'items' in response:
            return response['items']
        else:
            return []
    except vk_api.exceptions.ApiError:
        return []

# Функция для обработки пользователей и их друзей из members.csv
def process_members(file_name, token):
    # Авторизация в VK API
    vk_session = vk_api.VkApi(token=token)

    # Чтение файла с айди пользователей
    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок
        output_data = []
        for idx, row in enumerate(reader, start=1):
            user_id = row[0]
            friends = get_friends(vk_session, user_id)
            output_data.append([idx, user_id, ','.join(map(str, friends))])

    # Запись результатов в файл
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Index', 'User ID', 'Friends'])
        writer.writerows(output_data)

# Введите ваш токен доступа VK API
token = '3439c2983439c2983439c298af372e797e334393439c29851c41e311644bc350d290ea7'

# Вызов функции для обработки пользователей
process_members('members.csv', token)
