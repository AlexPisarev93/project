from settings import MY_PATH
import requests


def get_json() -> list:
    """Получение файла Json"""
    response = requests.request("get", MY_PATH)
    return response.json()




if __name__ == '__main__':
    pass