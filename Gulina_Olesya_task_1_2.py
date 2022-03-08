
#Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
my_list = []
idx = 1
while idx <= 1000:
    my_list.append(idx **3)
    idx += 2
final_sum = 0
for num in my_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum = num

print (final_sum)