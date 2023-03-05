from datetime import date

date_one = date(1815, 12, 12) # вывод 12 декабря 1815

print(date_one)



from datetime import time

time_one = time(16, 20, 00) # 16 часов 20 минут

print(time_one)


from datetime import datetime

datetime_one = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47

print(datetime_one)

# Методы datetime
# thedate.year
# Вернет год
# thedate.month
# Вернет месяц
# thedate.day
# Вернет день
# thedate.hour
# Вернет час
# thedate.minute
# Вернет минуту
# thedate.second
# Вернет секунду

# данный метод только для datetime
from datetime import datetime

thedate = datetime.now()

print(thedate)


# примеры методов тоже самое с time
from datetime import date

thedate = date.fromisoformat("2021-05-04")

print(thedate.year)
print(thedate.month)
print(thedate.day)

# Выведет:
# 2021
# 5
# 4


# вычисление разницы между датами
from datetime import date

# Задает первую дату
time_one = date(2020, 10, 1)
# Задает вторую дату
time_two = date(2020, 10, 2)

# Вычисляет расстояние в формате timedelta
delta = time_two - time_one

print(delta)

# Выведет 1 day, 0:00:00