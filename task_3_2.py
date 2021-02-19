# __author__* Соловьева Дарья Викторовна
# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
dict_num = {
    "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
    "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"
}


def num_translate_adv(num):
    get_num = dict_num.get(num.lower())
    if num.istitle() == True and get_num != None:
        return dict_num[num.lower()].capitalize()
    else:
        return dict_num.get(num)


print(num_translate_adv("Two"))