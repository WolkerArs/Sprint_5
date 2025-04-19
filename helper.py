import random

def generate_user():
    name = 'Арсений Дунаев'
    email = f'arsdunaev18{random.randint(100,999)}@mail.ru'
    password = random.randint(100000, 999999)
    return name, email, password