import requests

response = requests.get('https://catfact.ninja/fact')

# # Получение инфо html
# print(response.text)
#
# # Получение статус кода
# print(response.status_code)

# Что бы получить ключи с сайта
fact = response.json()
print(fact.keys())