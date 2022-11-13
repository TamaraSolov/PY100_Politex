def get_unique_list_numbers() -> list[int]:
    from random import randint
    list_int = [randint(-10, 10) for i in range(15)]
    a = set(list_int)
    return a
     # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
