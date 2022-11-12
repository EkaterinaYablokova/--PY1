import random

def get_unique_list_numbers() -> list[int]:
    list_ = []
    number_already_exists = set()
    for i in range(15):
        number = random.randint(-10, 10)
        while number in number_already_exists:
            number = random.randint(-10, 10)
        number_already_exists.add(number)
        list_.append(number)
    return list_  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
