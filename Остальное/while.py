password = "Hello"
ps = ""
# прописываем != при не совпадение паролей цикл завершается.
while ps != password:
    ps = input("Введите пароль: ")

print("Вход в систему")



debit = 10000
cred = 0

while debit > 0:
    cred = int(input("Введите на сколько хотите погасить кредит: "))
    debit -= cred
    print(f"Осталось погасить: {debit}")

print("Все погашено")

