import requests
import json
from datetime import datetime


class User:
    def __init__(self, user_id_name, vk_token):
        self.user_id_name = user_id_name
        self.vk_token = vk_token

    def _userinfo_normalize(self):
        user_info = self._get_vk("users.get")
        if user_info:
            self.user_id = user_info["response"][0]["id"]
            self.username = user_info["response"][0]["screen_name"]
            self.first_name = user_info["response"][0]["first_name"]
            self.last_name = user_info["response"][0]["last_name"]
        else:
            self.user_id = None

    def _form_params(self, method):
        params = {
            "access_token": self.vk_token,
            "v": "5.131",
        }
        if method == "photos.get":
            params.update({
                "owner_id": self.user_id,
                "album_id": "profile",
                "extended": 1,
                "photo_sizes": 1
            })
        elif method == "users.get":
            params.update({
                "user_ids": self.user_id_name,
                "fields": "screen_name",
                "name_case": "gen"
            })
        else:
            print("Неверно задан метод")
        return params

    def _get_vk(self, method):
        api = "https://api.vk.com/method/" + method
        params = self._form_params(method)
        response = requests.get(api, params)
        getting_info = response.json()
        try:
            if getting_info["response"]:
                pass
        except KeyError:
            try:
                if getting_info["error"]["error_code"] == 113:
                    print("Пользователь с указанным id/username не найден")
                else:
                    print(getting_info["error"]["error_msg"])
            except KeyError:
                print("Неизвестная ошибка")
            finally:
                getting_info = None
        finally:
            return getting_info

    def get_name_url(self):
        self._userinfo_normalize()
        if self.user_id:
            photo_list = []
            photo_file_names = []
            items = self._get_vk("photos.get")
            items = items["response"]["items"]
            for item in items:
                name = str(item["likes"]["count"])
                date = item["date"]
                if item["sizes"][len(item["sizes"]) - 1]["type"] == "s" and len(item["sizes"]) > 1:
                    i = 2
                else:
                    i = 1
                url = item["sizes"][len(item["sizes"]) - i]["url"]
                size = item["sizes"][len(item["sizes"]) - i]["type"]
                photo_list.append({'file_name': name, 'date': date, 'url': url, 'size': size})
            print(f"Получена информация о фотографиях {self.first_name} {self.last_name}")
        else:
            photo_list = []
        return photo_list


class FileUpload:
    def __init__(self, files, ya_token):
        self.files = files
        self.ya_token = ya_token

    def _get_headers(self):
        return {'Connect-Type': 'application/json', 'Authorization': self.ya_token}

    def _check_path(self, folder):
        headers = self._get_headers()
        check_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        params = {"path": folder, "fields": "path"}
        checking = requests.get(check_url, headers=headers, params=params)
        if checking.status_code == 404:
            print(f"Создаем папку {path}")
            create_folder = requests.put(check_url, headers=headers, params={"path": folder})
            create_folder.raise_for_status()
            if create_folder.status_code == 201:
                print("Папка создана. Приступаем к загрузке")
            else:
                error_msg = create_folder.json()
                print(error_msg["message"])
                folder = None
        else:
            print(f"Приступаем к загрузке в папку {folder}")
        return folder

    def upload(self, ya_path, count=5):
        ya_path = self._check_path(ya_path)
        if ya_path:
            headers = self._get_headers()
            files = self.files
            photo_names = []
            status = []
            count_in_list = len(files)
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
            if count > count_in_list:
                count = count_in_list
            for file_index in range(count_in_list, count_in_list - count, -1):
                file_name = files[file_index - 1]["file_name"]
                if file_name in photo_names:
                    photo_date = files[file_index - 1]["date"]
                    photo_date = datetime.utcfromtimestamp(photo_date).strftime('%Y-%m-%d')
                    file_name = f'{file_name}_{photo_date}'
                else:
                    photo_names.append(file_name)
                file_name += ".jpg"
                file_url = files[file_index - 1]["url"]
                params = {"path": f"{ya_path}/{file_name}", "url": file_url}
                uploading = requests.post(upload_url, headers=headers, params=params)
                uploading.raise_for_status()
                if uploading.status_code == 202:
                    print(f'Загружена фотография {count_in_list - file_index + 1} из {count}')
                    status.append({"file_name": file_name, "size": files[file_index - 1]["size"]})
            with open("report.json", "w") as report_file:
                json.dump(status, report_file)
        else:
            print("Операция прервана из-за ошибки")


if __name__ == "__main__":
    act_vk_token = ""
    act_ya_token = ""
    user1 = input("Введите id или username: ")
    photo_count = int(input("Введите количество фотографий: "))
    upload = User(user1, act_vk_token)
    upload_list = upload.get_name_url()
    path = upload.username
    FileUpload(upload_list, act_ya_token).upload(path, photo_count)