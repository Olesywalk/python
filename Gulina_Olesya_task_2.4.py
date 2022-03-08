# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих
# имён и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить
# имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in bad_list:
    if isinstance(position, str):
        print('Привет,',position.split()[-1].title(),'!')
    else:
        print('Error')