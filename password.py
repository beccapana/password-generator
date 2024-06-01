import datetime
import os
import random
import string
import psutil

def get_connection_type():
    connections = psutil.net_if_addrs()
    if 'eth0' in connections:  # проверка наличия проводного подключения
        return 'wired'
    elif 'wlan0' in connections:  # проверка наличия беспроводного подключения
        return 'wireless'
    else:
        return 'unknown'

def get_active_process_count():
    return len(psutil.pids())

def generate_password(length=12, use_special_chars=True, use_uppercase=True):
    date_time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    connection_type = get_connection_type()
    active_process_count = get_active_process_count()

    # Основной набор символов
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special_chars:
        characters += string.punctuation
    characters += string.digits

    # Инициализация генератора случайных чисел
    random.seed(date_time_str + connection_type + str(active_process_count))

    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Пример использования
length = int(input("Введите длину пароля: "))
use_special_chars = input("Использовать спецсимволы? (да/нет): ").lower() == 'да'
use_uppercase = input("Использовать прописные буквы? (да/нет): ").lower() == 'да'

password = generate_password(length, use_special_chars, use_uppercase)
print("Сгенерированный пароль:", password)
