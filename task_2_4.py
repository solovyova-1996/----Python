# __author__* Соловьева Дарья Викторовна

# 4. Создать список, содержащий цены на товары (10 – 20 товаров), например: [57.8, 46.51, 97, ...]
# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

price_list = [57.8, 46.51, 77, 93.9, 5, 90, 12.22, 53.44, 5.9, 66.66, 8, 100, 33.4, 88, 7]

for price in price_list[:]:
    type_price_int = isinstance(price, int)
    if type_price_int == True:
        index_price = price_list.index(price)
        new_price = f"{price} руб 00 коп"
        price_list[index_price] = new_price
    else:
        index_price = price_list.index(price)
        price = str(price)
        rub = price[:price.index('.')]
        cop = price[price.index('.'):]
        if len(cop) < 3:
            new_price = f"{rub} руб 0{cop} коп"
        else:
            new_price = f"{rub} руб {cop} коп"
        new_price = new_price.replace(".", "")
        price_list[index_price] = new_price

str_price_list = ",".join(price_list)
print(str_price_list)

# - Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

price_list = [57.8, 46.51, 77, 93.9, 5, 90, 12.22, 53.44, 5.9, 66.66, 8, 100, 33.4, 88, 7]
print("Объект списка до сортировки: ", price_list[4], "id объекта списка до сортировки: ", id(price_list[4]))
price_list.sort()
print("Объект списка после сортировки: ", price_list[0], "id объекта списка после сортировки: ", id(price_list[0]))

# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.

price_list = [57.8, 46.51, 77, 93.9, 5, 90, 12.22, 53.44, 5.9, 66.66, 8, 100, 33.4, 88, 7]
price_list_s = sorted(price_list, reverse=True)
print(price_list_s)

# - Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [57.8, 46.51, 77, 93.9, 5, 90, 12.22, 53.44, 5.9, 66.66, 8, 100, 33.4, 88, 7]
price_list.sort()
for price in price_list[len(price_list) - 5:]:
    max_price = price_list.pop()
    print(max_price)