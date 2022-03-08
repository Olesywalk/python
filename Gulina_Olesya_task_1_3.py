#Реализовать склонение слова «процент» во фразе «N процентов».
#Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100

percent = int(input("Введите число процента:"))

if percent == 1:
    word = "процент"
elif percent <= 4:
    word = "процент"
else:
    word = "процентов"
    print (percent, word)

for number in range(1,101):
    if 4 < number % 100 <= 20:
        print (f'{number} процентов')
    elif number % 10 == 1:
        print(f'{number} процент')
    elif 1 < number % 10 < 5:
        print(f'{number} процента')
    else:
        print(f'{number} процентов')



