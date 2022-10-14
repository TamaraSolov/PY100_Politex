list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
s = set(list_)
sum_ = sum(s)
print(sum_)
quan = len(s)
print(quan)
mean_ = round(sum_/quan,5)
print(mean_)