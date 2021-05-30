import requests
import json
from datetime import datetime


class User:
    def __init__(self, user_id, vk_token, ya_token):
        self.user_id = user_id
        self.vk_token = vk_token
        self.ya_token = ya_token

    def _get_photo_info(self):
        api = "https://api.vk.com/method/photos.get"
        params = {
            "access_token": self.vk_token,
            "owner_id": self.user_id,
            "v": "5.131",
            "album_id": "profile",
            "extended": 1,
            "photo_sizes": 1
        }
        response = requests.get(api, params)
        getting_info = response.json()
        print('Получен ответ от сервера VK')
        return getting_info

    def get_name_url(self):
        photo_list = []
        photo_file_names = []
        items = self._get_photo_info()
        photo_list.append(items['response']['count'])
        items = items['response']['items']
        for item in items:
            name = str(item['likes']['count'])
            if name in photo_file_names:
                photo_date = item['date']
                photo_date = datetime.utcfromtimestamp(photo_date).strftime('%Y-%m-%d')
                name = f'{name}_{photo_date}'
            else:
                photo_file_names.append(name)
            if item['sizes'][len(item['sizes']) - 1]['type'] == 's' and len(item['sizes']) > 1:
                i = 2
            else:
                i = 1
            url = item['sizes'][len(item['sizes']) - i]['url']
            size = item['sizes'][len(item['sizes']) - i]['type']
            photo_list.append({'file_name': name + '.jpg', 'url': url, 'size': size})
        print('Получена информация о фотографиях')
        return photo_list

    def _get_headers(self):
        return {'Connect-Type': 'application/json', 'Authorization': self.ya_token}

    def upload(self, count=5):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self._get_headers()
        file_info = self.get_name_url()
        status = []
        if count > file_info[0]:
            count = file_info[0]
        for i in range(file_info[0], file_info[0] - count, -1):
            file_name = file_info[i]['file_name']
            file_url = file_info[i]['url']
            params = {'path': f'PYTest/{file_name}', 'url': file_url}
            uploading = requests.post(upload_url, headers=headers, params=params)
            uploading.raise_for_status()
            if uploading.status_code == 202:
                print(f'Загружена фотография {file_info[0] + 1 - i} из {count}')
                status.append({'file_name': file_name, 'size': file_info[i]['size']})
        with open('report.json', 'w') as report_file:
            json.dump(status, report_file)


act_vk_token = ''
act_ya_token = ''
user1 = 552934290
User(user1, act_vk_token, act_ya_token).upload(2)