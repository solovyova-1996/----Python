# __author__ * Соловьева Дарья Викторовна
# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}}
# Сможете ли вы вернуть отсортированный по ключам словарь?

name_dict_new = {}
name_dict = {}


def thesaurus_adv(*args):
    for name in args:
        index_surname = name.index(" ") + 1
        if name_dict.get(name[index_surname]) != None:
            if name_dict[name[index_surname]].get(name[0]) != None:
                name_dict[name[index_surname]][name[0]].append(name)
            else:
                name_dict[name[index_surname]].setdefault(name[0], [name])

        else:
            dict_name = {name[index_surname]: {name[0]: [name]}}
            name_dict.update(dict_name)
    # сортировка словаря по ключам
    
    for k in sorted(name_dict.keys()):
        new_dict = {k: name_dict[k]}
        name_dict_new.update(new_dict)

    return name_dict_new


print(thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    "Василий Суриков"))