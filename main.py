"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
затем выведите на экран.
"""

# начало
greeting_test = 'ДЗ по курсу Знакомство с Питоном - первый урок'
print(greeting_test)
# ну тоже начало
print("Привет пользователь! Введи пару чилес а я умножу их почти как Алиса))")
fist_el = int(input("Первое число:"))
second_el = int(input("Второе число:"))
print(f'Бац...Вот результать: { fist_el * second_el }')

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

print()
print('2 задача')
print()
time_in_seconds = int(input("Пользователь введи любое число не меньше 1 и я превращу его в часы минуты и секунды:"))
# получаем часов
hour = time_in_seconds // 3600

# из остатка от деления получаем минуты
remains_of_seconds = time_in_seconds % 3600
minutes = remains_of_seconds // 60

# из остаток полсле вычисления минты получаем секунды
seconds = remains_of_seconds % 60
print(f'Время {hour} : {minutes} : {seconds}')

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
print()
print('3 задача')
print()
n_o_u = input("Введите любое число: ")
summa_of_number = int(n_o_u) + int(n_o_u + n_o_u) + int(n_o_u + n_o_u + n_o_u)
print(f'Считаем {n_o_u} + {n_o_u+n_o_u} + {n_o_u+n_o_u+n_o_u} = {summa_of_number}')


"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""
print()
print('4 задача')
print()
integer = input("Введите целое положительное число: ")
check = True
n = 0
if n < 9:
    while check:
        print(f"Делим число {integer} // 10  = {int(integer) // 10}")
        print(f"Делим число {integer} % 10  = {int(integer) % 10}")
        remains_n = int(integer) // 10
        last_n = int(integer) % 10
        print(f" результать ц. деления {remains_n} ")
        print(f" последняя цифра {last_n}")
        # если результат деления вернула 0 значит цифры закончились и мы прерываем цикл
        if remains_n == 0:
            break
        # если последнная цифра больше предеушего то позьмем её
        if last_n > n:
            n = last_n
        integer = remains_n
    print("Самое большое число {:>10}".format(n))
else:
    print("Самое большое число {:>10}".format(integer))

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, 
с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, 
или убыток — издержки больше выручки. Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки. 
Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчёте на одного сотрудника.
"""
print()
print('5 задача')
print()
print("'Анализатор'")
income = int(input("Введите выручку фирмы в рублях: "))
cost = int(input("Введите издержки фирмы в рублях: "))
if income > cost:
    q = input("О! У вас прибыл:) Давайте я вам посчитаю рентабельность выручки? (да/нет)")
    if q != "нет" or q != "no":
        # вычисляем прибыль
        p = income - cost
        # вычисляем рентабельность
        profitability = p/income
        print(f"Рентабельность выручки состовляет: {profitability}")
        # далее посчитаем прибыл на одного сотрудника
        number_of_personnel = int(input("Ввыведите численность персонала: "))
        profit_to_person = p / number_of_personnel
        print(f"Прибыль фирмы в расчёте на одного сотрудника состовляет: {profit_to_person} р.")
    else:
        print("Как вам угодно!")
else:
    # вычисляем убыток
    t = cost - income
    print(f"У вас прбыла нет! Ваша убыток = {t}")

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. 
Требуется определить номер дня, на который результат спортсмена составит 
не менее b километров. Программа должна принимать значения параметров a и b и 
выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат: 
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км. 
"""
print()
print('5 задача')
print()
print("Шагомер")
a = int(input("Введите результать первый день пробежки в км (a): "))
b = int(input("Введите цель в км(b): "))
c = 1
# while a < b:
while True:
    print("{}-й день: {:.2f}".format(c, a))
    tp = (a / 100) * 10
    if a >= b:
        break
    a = tp + a
    c += 1









