# __author__ * Соловьева Дарья Викторовна
# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
#
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import randrange


def get_jokes(n):
    """
    Сreates jokes from three random words
    :param n: number of jokes
    :return: list of n-jokes
    """

    joke_list = []
    for i in range(n):
        joke = f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} " \
               f"{adjectives[randrange(len(adjectives))]}"
        joke_list.append(joke)

    return joke_list


print(get_jokes(3))


# Усложнение: * Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


def get_jokes_repeat(n=1, repeat_words_ban=True):
    """
    Сreates jokes from three random words
    :param n: number of jokes
    :param repeat_words_ban: True - words are not repeated
    :return: list of  n-jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke_list = []

    for i in range(n):
        if repeat_words_ban:
            joke = f"{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))} " \
                   f"{adjectives.pop(randrange(len(adjectives)))}"
        else:
            joke = f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} " \
                   f"{adjectives[randrange(len(adjectives))]}"
        joke_list.append(joke)

    return joke_list

# запрещает повтор
print(get_jokes_repeat(n=4))
# разрешает повтор
print(get_jokes_repeat(n=4,repeat_words_ban=False))