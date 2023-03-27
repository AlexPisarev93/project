# Чтобы установить пакет, выполните команду:
# pip install package-name

# Альтернативный способ, который устанавливает пакет для конкретной версии Python:
# python3.7 -m pip install package-name

# Флаг -m сообщает Python запустить pip как исполняемый модуль.
# Иногда при установке очередного пакета появляется сообщение о том, что доступна новая версия pip:

# WARNING: You are using pip version 19.2.3, however version 19.3.1is available.
# В этом случае воспользуйтесь командой для обновления pip:

# python3 -m pip install --upgrade pip


# pip help
# Что бы ознакомится со всеми Основными командами при работе с pip:

# pip install package-name
#  — устанавливает последнюю версию пакета.

# pip install package-name==4.8.2
#  — устанавливает пакет версии 4.8.2.

# pip install package-name --upgrade
#  — обновляет версию пакета.

# pip install --user package-name
#  — устанавливает пакет в глобальное окружение текущего пользователя.

# pip install -r requirements.txt
#  — устанавливает библиотеки, перечисленные в txt-файле.

# pip uninstall package-name
#  — удаляет пакеты.

# pip freeze
#  — выводит список установленных пакетов в необходимом формате, обычно в requirements.txt.

# pip list
#  — выводит список установленных пакетов.

# pip list --outdated
#  — выводит список устаревших пакетов.

# pip show package-name
#  — показывает информацию об установленном пакете