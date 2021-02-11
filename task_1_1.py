duration = int(input("Введите продолжительность времени в секундах: "))
minutes = duration // 60
seconds = duration - minutes * 60
hour = duration // 3600
# секунд в дне 86400
days = duration // 86400
if duration < 60:
    print(duration, "сек")
elif 60 <= duration < 3600:
    print(minutes, "мин", seconds, "сек")
elif 3600 <= duration < 86400:
    minutes = (duration - hour * 3600) // 60
    seconds = duration - (minutes * 60 + hour * 3600)
    print(hour, " час", minutes, "мин", seconds, "сек")
else:
    hour = (duration - days * 86400) // 3600
    minutes = (duration - (days * 86400 + hour * 3600)) // 60
    seconds = duration - ((days * 86400) + (hour * 3600) + (minutes * 60))
    print(days, "дн", hour, "час", minutes, "мин", seconds, "сек")
