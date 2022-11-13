from random import choice
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

def first_hod(f = "X",s ="0"):
    player = [f, s]
    cur_pla = choice (player)
    return cur_pla

def result(player):
    # Функция определяет результат игры после прохождения по всем возможным выигрышным комбинациям
    # В цикле for перебираем победные комбинациям по индексам внутри большого списка и индесам
    # внутри каждого маленького списка
    pobeda = ""

    for i in vin_combination:
        if pole[i[0]] == player and pole[i[1]] == player and pole[i[2]] == player:
            pobeda = player

    return pobeda
def proverka (start, finish):
    while True:
        try:
            step_ = int(input(f"{igrok} игрок введите цифру от 1 до 9: "))  # вводить можно только цифры от 1 до 9
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз")
        else:
            if start <= step_ <= finish:
                return step_
            print(f"Веденное число вне диапазона от {start} до {finish}")

# Тело программы
# Предполагаем что игра не кончилась, первый ход "крестиком" делает 1 игрок
# в позицию на поле от 1 до 9
if __name__ == "__main__":
    game = True
    # igrok = "X"
    igrok = first_hod()
    count = 0

    while game == True:
        print_pole()# Печатаем поле из цифр для игры
        step = proverka(1,9)
        # step = int(input(f"{igrok} игрок введите цифру от 1 до 9: "))  # вводить можно только цифры от 1 до 9

        do_step(pole, step, igrok)
        count += 1
        # делаем ход в указанную ячейку на поле
        pobeda = result(igrok)  # определяем кто победил, "крестики" или "нолики"
        if pobeda != "":  # если победитель определен заканчиваем игру
            game = False
        else:
            game = True  # если нет, продолжаем игру
        igrok = "X" if igrok == "0" else "0" # переход хода другому игроку

    print_pole()  # Печатаем итоговое поле игры и выводим победителя
    if count < 9:
        print("Победили", pobeda)
    else:
        print("Ничья")