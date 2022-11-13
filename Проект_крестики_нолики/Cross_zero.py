pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Массив цифр для поля игры
# Игрок может вводить цифру только от 1 до 9

vin_combination = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
# Прописываем варианты выигрышных комбинаций игры в виде списка списков

def print_pole():# Рисуем поле на экране
    print(pole[0], end=" ")
    print(pole[1], end=" ")
    print(pole[2])

    print(pole[3], end=" ")
    print(pole[4], end=" ")
    print(pole[5])

    print(pole[6], end=" ")
    print(pole[7], end=" ")
    print(pole[8])

def do_step(pole, step, x_o):
    # Функция делает ход в нужную ячейку на поле
    # принимает входные значения:
    # pole: поле
    # step: шаг (номер ячейки в самом поле)
    # x_o: крестик (х) или нолик (о)
    index_ = pole.index(step)
    pole[index_] = x_o
    return x_o

def result():
    # Функция определяет результат игры после прохождения по всем возможным выигрышным комбинациям
    # В цикле for перебираем победные комбинациям по индексам внутри большого списка и индесам
    # внутри каждого маленького списка
    pobeda = ""

    for i in vin_combination:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
            pobeda = "Крестики"
        if pole[i[0]] == "O" and pole[i[1]] == "O" and pole[i[2]] == "O":
            pobeda = "Нолики"

    return pobeda

# Тело программы
# Предполагаем что игра не кончилась, первый ход "крестиком" делает 1 игрок
# в позицию на поле от 1 до 9
game = True
igrok1 = True
igrok2 = False

while game == True:

    print_pole()     # Печатаем поле из цифр для игры

    if igrok1 == True: # Запрашиваем у игрока в какую позицию делать ход и
        # ставим туда соответственно "крестик" или "нолик"
        x_o = "X"
        step = int(input("Первый игрок введите цифру от 1 до 9: ")) # вводить можно только цифры от 1 до 9
    else:
        x_o = "O"
        step = int(input("Второй игрок введите цифру от 1 до 9: "))

    do_step(pole, step, x_o)
    # делаем ход в указанную ячейку на поле
    pobeda = result()  # определяем кто победил, "крестики" или "нолики"
    if pobeda != "":  # если победитель определен заканчиваем игру
        game = False
    else:
        game = True   # если нет, продолжаем игру

    igrok1 = not (igrok1) # переход хода другому игроку

print_pole() # Печатаем итоговое поле игры и выводим победителя
print("Победили", pobeda)