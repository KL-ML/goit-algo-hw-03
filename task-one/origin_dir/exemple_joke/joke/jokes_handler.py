import random
import pathlib

current_dir = pathlib.Path(__file__).parent # визначає директорію, де знаходиться файл скрипту. Нам це необхідно, щоб шлях до файлу current_dir / "jokes.txt" завжди був вірний де б ми не виконали нашу програму

def get_random_joke(): # Цей код визначає функцію get_random_joke(), яка відкриває файл jokes.txt, розташований у тій же директорії, що й сам скрипт, і вибирає з нього випадковий анекдот
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file: # файл jokes.txt відкривається за допомогою контекстного менеджера with, що гарантує правильне закриття файлу після завершення роботи з ним
            jokes = file.readlines() # Анекдоти з файлу читаються у список jokes
            return random.choice(jokes).strip() # з якого потім випадковим чином вибирається один за допомогою random.choice(jokes)
    except FileNotFoundError: # Якщо файл jokes.txt не знайдено, функція повертає рядок "Не вдалося знайти файл з анекдотами.", щоб проінформувати користувача про помилку
        return "Не вдалося знайти файл з анекдотами."
