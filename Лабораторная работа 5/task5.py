from random import sample
import string

symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
lenght = 8


def get_random_password() -> str:
    return "".join(sample(symbols, lenght))  # TODO написать функцию генерации случайных паролей


print(get_random_password())
