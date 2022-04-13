# 2. * (вместо задачи 1)
# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


eng_rus_dict = {                     #Создали словарь {ключ:значение, в ключе английское слово, в значении русский перевод}
    'one':'один',
    'two': 'два',
    'three':'три',
    'four':'четыре',
    'five': 'пять',
    'six':'шесть',
    'seven':'семь',
    'eight':'восемь',
    'nine':'восемь',
    'ten': 'десять'
}

def num_translate_adv(eng_word):                     #Создали функцию, которая, принимает в качестве аргумента анг.числ.
    if not eng_rus_dict.get(eng_word.lower()):               #Если слово не числительное на английском, то выводим
        return None
    elif eng_word[0] ==eng_word[0].upper():                  #Если первая буква в английском слове большая, а
        eng_word = eng_word.lower()                          # все остальные маленькие
        return eng_rus_dict[eng_word].capitalize()           # выводим значение с большой буквы
    else:
        return eng_rus_dict[eng_word]

print(num_translate_adv('khgfgjf'))
print(num_translate_adv('ten'))
print(num_translate_adv('Ten'))