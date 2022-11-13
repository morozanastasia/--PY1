import random


def get_unique_list_numbers() -> list[int]:

    list_unique_numbers = []

    min_value = -10
    max_value = 10
    size = 15

    while len(list_unique_numbers) < size:
        num = random.randint(min_value, max_value)
        if num not in list_unique_numbers:
            list_unique_numbers.append(num)
    return list_unique_numbers








list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
