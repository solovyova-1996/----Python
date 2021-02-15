# __author__* Соловьева Дарья Викторовна
# 2.Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку
# до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание:
# - Задача обычной сложности: создайте новый список и заполните его нужными значениями, включая элементы-кавычки,
# например: ['в', '"', '05', '"', 'часов',...] или измените существующий список, но не добавляйте новые элементы-кавычки,
# кавычки сразу внесите в элемент-число, например: ['в', '"05"', 'часов',...]
# - * Задача повышенной сложности: измените существующий список, и добавьте элементы-кавычки.
# Эта задача намного серьезнее,  чем может сначала показаться.
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Вывести список и строку на экран. Обратите внимание на отсутствие "лишних" пробелов около кавычек.

weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
quotes = '"'
print(id(weather_list), weather_list)

for element_list in weather_list[:]:

    for i in element_list:
        i = str(i)
        type_i = i.isdigit()

        if type_i == True and len(element_list) < 2:
            index_element_list = weather_list.index(element_list)
            new_element_list = f"0{element_list[0]}"
            weather_list[index_element_list] = new_element_list
            weather_list.insert(index_element_list, quotes)
            weather_list.insert(index_element_list + 2, quotes)
        elif type_i == True and len(element_list) >= 2 and (element_list[0] == "+" or element_list[0] == "-"):
            index_element_list = weather_list.index(element_list)
            new_element_list = "{}0{}".format(element_list[0], element_list[1])
            weather_list[index_element_list] = new_element_list
            weather_list.insert(index_element_list, quotes)
            weather_list.insert(index_element_list + 2, quotes)

    if element_list.isdigit() == True and len(element_list) >= 2:
        index_element_list = weather_list.index(element_list)
        weather_list.insert(index_element_list, quotes)
        weather_list.insert(index_element_list + 2, quotes)

print(id(weather_list), weather_list)

print(
    f"{weather_list[0]} {''.join(weather_list[1:4])} {weather_list[4]} {''.join(weather_list[5:8])} {weather_list[8]} "
    f"{weather_list[9]} {weather_list[10]} {weather_list[11]} {''.join(weather_list[12:15])} {weather_list[15]}")