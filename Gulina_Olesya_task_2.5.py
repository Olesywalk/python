# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в
# виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить
# рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
#
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать,
# что объект списка после сортировки остался тот же).
#
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров
# по возрастанию, написав минимум кода?


goods = [66.7, 59.99, 10, 47.99, 20.14, 66.18, 40.05, 50.98, 90.77, 1]
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой



goods = []
print(id(goods))
print(goods)
goods.sort()
print(id(goods))
print(goods)
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой


goods = [66.7, 59.99, 10, 47.99, 20.14, 66.18, 40.05, 50.98, 90.77, 1]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой

# one line
print([f'{int(good)} руб {(good - int(good)) * 100:02.0f} коп' for good in sorted(goods)[::-1][:5]])