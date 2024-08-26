import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный статус-код
        data = response.json()
        return data[0]['url'] if data else None  # Возвращаем URL изображения
    except requests.RequestException:
        return None  # Возвращаем None при ошибке запроса