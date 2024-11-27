import random
import time

# Список слов для генерации мемов
words = [
    "кто такой алексей???", "20:31", "чиназес", "имба", "скуф", "скам", "альтушка с госуслуг", "хайп", "причина тряски", "биток по 100к"
]

def generate_meme_phrase():
    return f"{random.choice(words)}"

# Бесконечный цикл для генерации и вывода фраз-мемов
while True:
    print(generate_meme_phrase())
    time.sleep(0.5) 