money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
b = money_capital + salary

month = 0  # количество месяцев, которое можно прожить
while b > 0:
    b = b - spend
    spend *= 1 + increase
    month += 1
    # if b > 0:
    #     b = b - (spend + (spend*increase))
    #     month +=1
# TODO Оформить решение
print(month)
"""

"""
