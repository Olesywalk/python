#1.1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input ('Введите время в секундах:'))
days = duration // (60 * 60 * 24)
hours = (duration - days *(60 * 60 * 24)) // (60 * 60)
minutes = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
seconds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print (days,'дн',hours,'час',minutes,'мин',seconds,'сек')