import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.token = ''

    def get_headers(self):
        return {'Connect-Type': 'application/json', 'Authorization': self.token}

    # def get_file_info(self):
    #     files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files/'
    #     headers = self.get_headers()
    #     response = requests.get(files_url, headers=headers)
    #     return response.json()

    def _get_file_name(self):
        split_path = self.file_path.split("\\")
        return split_path[len(split_path)-1]

    def upload(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': f'PYTest/{self._get_file_name()}', 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        response = response.json()
        href = response['href']
        uploading = requests.put(href, data=open(self.file_path, 'rb'))
        uploading.raise_for_status()
        if uploading.status_code == 201:
            print('Файл загружен')
    #
    #     """Метод загруджает файлы по списку file_list на яндекс диск"""
    #     # Тут ваша логика
    #     return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader(r"D:\Content\123.txt")
    result = uploader.upload()