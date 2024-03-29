import vk_api
import csv


# Функция для получения всех постов со стены группы
def get_all_group_posts(group_domain, token):
    # Авторизация
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    # Список для хранения всех постов
    all_posts = []

    # Начинаем считывать посты, пока они не закончатся
    offset = 0
    count = 100  # Максимальное количество постов, которые можно получить за один запрос
    while True:
        posts = vk.wall.get(domain=group_domain, count=count, offset=offset)
        all_posts.extend(posts['items'])
        if offset >= posts['count']:
            break
        offset += count

    return all_posts


# Функция для записи данных в CSV файл с добавлением ссылки на сохраненный пост
def write_to_csv(posts, filename):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID поста', 'Текст поста', 'Ссылки на изображения', 'Ссылка на сохраненный пост'])
        for post in posts:
            post_id = post['id']
            text = post.get('text', '')
            attachments = post.get('attachments', [])
            photo_links = []
            for attachment in attachments:
                if attachment['type'] == 'photo':
                    photo = attachment['photo']
                    photo_links.append(photo['sizes'][-1]['url'])
            # Формирование ссылки на сохраненный пост
            post_link = f"https://vk.com/wall{post['owner_id']}_{post_id}"
            writer.writerow([post_id, text, ', '.join(photo_links), post_link])


if __name__ == "__main__":
    # Домен группы
    group_domain = 'rozyskdonbass'  # Укажите домен группы
    # Токен доступа
    token = '3439c2983439c2983439c298af372e797e334393439c29851c41e311644bc350d290ea7'  # Укажите свой токен доступа
    # Имя файла для сохранения данных
    filename = 'group_posts.csv'

    # Получение всех постов
    all_posts = get_all_group_posts(group_domain, token)

    # Запись данных в CSV файл
    write_to_csv(all_posts, filename)

    print(f'Все посты успешно сохранены в файл: {filename}')

# ----------------------------


# import vk_api
# import csv
#
#
# # Функция для получения всех участников группы
# def get_group_members(group_id, token):
#     # Авторизация
#     vk_session = vk_api.VkApi(token=token)
#     vk = vk_session.get_api()
#
#     # Получение списка участников группы
#     members = vk.groups.getMembers(group_id=group_id, fields="sex, bdate, city, country")
#
#     return members['items']
#
#
# # Функция для записи данных в CSV файл
# def write_to_csv(members, filename):
#     with open(filename, mode='w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['ID', 'Имя', 'Фамилия', 'Пол', 'Дата рождения', 'Город', 'Страна'])
#         for member in members:
#             member_id = member['id']
#             first_name = member.get('first_name', '')
#             last_name = member.get('last_name', '')
#             sex = member.get('sex', '')
#             bdate = member.get('bdate', '')
#             city = member.get('city', {}).get('title', '')
#             country = member.get('country', {}).get('title', '')
#             writer.writerow([member_id, first_name, last_name, sex, bdate, city, country])
#
#
# if __name__ == "__main__":
#     # Идентификатор группы
#     group_id = 'rozyskdonbass'  # Укажите ID группы
#     # Токен доступа
#     token = '3439c2983439c2983439c298af372e797e334393439c29851c41e311644bc350d290ea7'  # Укажите свой токен доступа
#     # Имя файла для сохранения данных
#     filename = 'group_members.csv'
#
#     # Получение всех участников
#     all_members = get_group_members(group_id, token)
#
#     # Запись данных в CSV файл
#     write_to_csv(all_members, filename)
#
#     print(f'Все участники успешно сохранены в файл: {filename}')

# -----------------------------------------


# import vk_api
# import csv
#
# # Функция для получения постов со стены группы
# def get_group_posts(group_id, count=10):
#     # Авторизация
#     vk_session = vk_api.VkApi()  # Введите свои данные для авторизации
#     vk_session.auth()
#     vk = vk_session.get_api()
#
#     # Получение постов со стены группы
#     posts = vk.wall.get(owner_id='-' + str(group_id), count=count)
#
#     return posts['items']
#
# # Функция для записи данных в CSV файл
# def write_to_csv(posts, filename):
#     with open(filename, mode='w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['ID поста', 'Текст поста', 'Ссылки на изображения'])
#         for post in posts:
#             post_id = post['id']
#             text = post.get('text', '')
#             attachments = post.get('attachments', [])
#             photo_links = []
#             for attachment in attachments:
#                 if attachment['type'] == 'photo':
#                     photo = attachment['photo']
#                     photo_links.append(photo['sizes'][-1]['url'])
#             writer.writerow([post_id, text, ', '.join(photo_links)])
#
# if __name__ == "__main__":
#     # Идентификатор группы
#     group_id = 'идентификатор_группы'  # Укажите ID группы
#     # Количество постов для сбора
#     count = 10  # Укажите количество постов, которое нужно собрать
#     # Имя файла для сохранения данных
#     filename = 'group_posts.csv'
#
#     # Получение постов
#     posts = get_group_posts(group_id, count)
#
#     # Запись данных в CSV файл
#     write_to_csv(posts, filename)
#
#     print(f'Посты успешно сохранены в файл: {filename}')
#


# -------------------------------------------
# import vk_api
# import time
# import os
# import csv
#
# # Введите сюда ваш access_token
# access_token = '3439c2983439c2983439c298af372e797e334393439c29851c41e311644bc350d290ea7'
#
# # ID группы
# group_id = 'rozyskdonbass'
#
# # Количество записей для сбора
# count = 5
#
# # Путь для сохранения изображений
# image_dir = 'images'
#
# # Авторизация
# vk = vk_api.VkApi(token=access_token)
#
#
# # Получение записей со стены
# def get_wall_posts(group_id, count):
#     posts = vk.wall.get(domain=group_id, count=count, filter='owner')
#     return posts['items']
#
#
# # Скачивание изображений
# def download_images(images, image_dir):
#     if not os.path.exists(image_dir):
#         os.makedirs(image_dir)
#
#     for image in images:
#         url = image['url']
#         filename = os.path.basename(url)
#         filepath = os.path.join(image_dir, filename)
#
#         # Скачивание изображения
#         with open(filepath, 'wb') as f:
#             response = vk.http.get(url)
#             f.write(response.content)
#
#
# # Запуск
# posts = get_wall_posts(group_id, count)
#
# # Скачивание изображений
# for post in posts:
#     if 'attachments' in post:
#         attachments = post['attachments']
#         images = [attachment for attachment in attachments if attachment['type'] == 'photo']
#         download_images(images, image_dir)
#
# # Задержка, чтобы не перегружать сервер
# time.sleep(5)
#
#
# # Функция для записи данных в CSV файл
# def save_to_csv(data, filename):
#     with open(filename, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=';')
#         writer.writerows(data)
#
#
# # Запись данных в CSV файл
# data = []
# for post in posts:
#     post_id = post['id']
#     text = post['text']
#     images = []
#
#     if 'attachments' in post:
#         attachments = post['attachments']
#         images = [attachment['photo']['sizes'][-1]['url'] for attachment in attachments if
#                   attachment['type'] == 'photo']
#
#     data.append([post_id, text, ';'.join(images)])
#
# save_to_csv(data, 'wall_posts.csv')
# -----------------------------------------
# import csv
#
# import requests
#
#
# def take_1000_posts():
#     token = '3439c2983439c2983439c298af372e797e334393439c29851c41e311644bc350d290ea7'
#     version = 5.199
#     domain = 'rozyskdonbass'
#     url = 'https://api.vk.com/method/wall.get'
#     count = 100
#     offset = 0
#     all_posts = []
#
#     while offset < 1000:
#         response = requests.get(url, params={'access_token': token,
#                                              'v': version,
#                                              'domain': domain,
#                                              'count': count,
#                                              'offset': offset
#                                              }
#                                 )
#         data = response.json()['response']['items']
#         offset += 100
#         all_posts.extend(data)
#     return all_posts
#
#
# def file_writer(data):
#     with open('posts.csv', 'w') as file:
#         a_pen = csv.writer(file)
#         a_pen.writerow(['likes', 'body', 'url'])
#         for post in data:
#             try:
#                 if post['attachments'][0]['type']:
#                     img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
#                 else:
#                     img_url = 'pass'
#             except:
#                 pass
#
#             a_pen.writerow((post['likes']['count'], post['text'], img_url))
#
#
#
#
# all_posts = take_1000_posts()
# file_writer(all_posts)
#
# print(1)
