from settings import MY_PATH
from classes import BasicWord, Player
import requests
import random


def get_json() -> list:
    """Получение файла Json"""
    response = requests.request("get", MY_PATH)
    return response.json()


def load_random_word():
    """- получит список слов с внешнего ресурса,
         выберет случайное слово,
         создаст экземпляр класса `BasicWord`,
         вернет этот экземпляр."""

    words = get_json()
    random_word = random.choice(words)
    word = random_word['word']
    subword = random_word['subwords']
    return BasicWord(word, subword)












