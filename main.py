import requests
import time
import logging

# Устанавливаем параметры запроса
url = 'https://api.binance.com/api/v1/ticker/price'
params = {'symbol': 'XRPUSDT'}
threshold = 1  # Задаем пороговое значение для анализа цены

# Получаем текущую цену и максимальную цену за последний час
response = requests.get(url, params=params).json()
current_price = float(response['price'])
max_price = float(response['price'])

# Запускаем программу в цикле
while True:

    try:
        # Считываем текущую цену и анализируем ее
        response = requests.get(url, params=params).json()
        current_price = float(response['price'])
        if (max_price - current_price) / max_price * 100 >= threshold:
            logging.warning(
                'Цена фьючерса XRP/USDT упала на 1% или более от максимальной цены за последний час!')
            print(
                'Цена фьючерса XRP/USDT упала на 1% или более от максимальной цены за последний час!')
    except:
        logging.error('Ошибка при получении данных')
    # Задержка перед следующим циклом
    time.sleep(60)
