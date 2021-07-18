import requests


def check_path(ya_token, folder):
    headers = {'Connect-Type': 'application/json', 'Authorization': ya_token}
    check_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    params = {"path": folder, "fields": "path"}
    checking = requests.get(check_url, headers=headers, params=params)
    status = checking.status_code
    if status == 404:
        print(f"Создаем папку {folder}")
        create_folder = requests.put(check_url, headers=headers, params={"path": folder})
        create_folder.raise_for_status()
        status = create_folder.status_code
        if status == 201:
            print("Папка создана")
        else:
            error_msg = create_folder.json()
            print(error_msg["message"])
            folder = None
    else:
        print(f"Папка {folder} создана ранее")
    return folder, status
