def get_count_char(str_):
    str_ = str_.lower()
    dict_ = {}

    for char in str_:
        if char.isalpha():
            if char in dict_:
                dict_[char] += 1
            else:
                dict_[char] = 1

    return dict_  # TODO посчитать количество каждой буквы в строке в аргументе str_


def percent_char(dict_):

    amount = sum(chars.values())
    for k in chars.keys():
        chars[k] = str(round(chars[k] / amount, 3) * 100) + '%'

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

chars = get_count_char(main_str)  # результат первой функции


print(get_count_char(main_str))
print(percent_char(chars))
