list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_ = list_numbers[0]
"""
for i in list_numbers:
    if i > max_:
        max_ = i
b = list_numbers.index(max_)
list_numbers[b]=list_numbers[-1]
list_numbers[-1]=max_
# TODO Оформить решение
"""
max_ = list_numbers[0]
for i, val in enumerate(list_numbers):
    if val > max_:
        max_ = val
        i_max = i
list_numbers[i_max], list_numbers[-1] = list_numbers[-1], list_numbers[i_max]
print(list_numbers)