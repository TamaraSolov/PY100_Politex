def get_count_char(str_):
    char_l = "".join((str_.lower().split()))
    char_list = list(char_l)

    dict_ = {}
    for i in char_list:
        if i in dict_:
            dict_[i] +=1
        else:
            dict_[i] = 1
    return dict_





    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
