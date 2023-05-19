#TASK 1
'''Написати і протестувати фун кцію, яка приймає один аргумент (рік) і повертає True, якщо рік є високосним, або False інакше.

Основу функції вже закладено у коді в редакторі.

Примітка: для вас підготувлено короткий тестуючий код, який можна використовувати для перевірки своєї функції.

У коді використовуються два списки - один із тестовими даними, інший - з очікуваними результатами. Код повідомить Вам, якщо якісь із Ваших результатів неправильні.'''


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = isLeapYear(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

"""Task 2
"""
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days_per_month = [31, 28 if not is_year_leap(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 29, 31]
    """
    Остальные дни в месяцах идут после else, потому что если введенный месяц не является февралем, то количество дней в нем будет одинаковым для всех лет. Таким образом, нет необходимости проверять наличие високосного года и можно просто вернуть количество дней для указанного месяца из массива dayspermonth.
    """
    return days_per_month[month-1] #"""Отнимаем единицу от month, потому что в массиве dayspermonth индексация начинается с нуля, а месяцы обычно нумеруются с единицы."""

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    re = test_results[i]
    print(yr, mo, re, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#TASK 3
"""def day_of_year(year, month, day):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_per_month[month-1]:
        return None
    if month == 2 and is_leap_year(year):
        days_per_month[1] = 29
    else:
        days_per_month[1] = 28
    day_of_year = sum(days_per_month[:month-1]) + day
    return day_of_year """

#task 4
"""
Ваше завдання - написати функцію, що перевіряє, чи є число простим чи ні.

Функція:

називається is_prime;
приймає один аргумент (значення для перевірки)
повертає True, якщо аргумент є простим числом, і False інакше.
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): #проверяем наличие делителей от 2 до корня из num + 1. Если num делится на одно из этих чисел без остатка - значит это не простое число.
        if num % i == 0:
            return False
    return True

# Test the function
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#task 5
"""Витрата палива автомобіля можна висловити по-різному. Наприклад, у Європі він відображається як кількість витраченого палива на 100 кілометрів шляху.

У США він відображається як кількість миль, пройдених автомобілем під час витрачання одного галону палива.

Ваше завдання - написати дві функції, що конвертують л/100км в миль на галон, і навпаки.

Функції:

названі liters_100km_to_miles_gallon та miles_gallon_to_liters_100km відповідно;
приймають один аргумент (значення, що відповідає їхнім іменам)"""

def liters_100km_to_miles_gallon(liters):
    miles = 100 / (liters / 3.785411784) / 1.609344
    return miles

def miles_gallon_to_liters_100km(miles):
    liters = 100 / (miles * 1.609344 / 3.785411784)
    return liters

print(liters_100km_to_miles_gallon(3.9)) # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5)) # 31.361944444444446
print(liters_100km_to_miles_gallon(10.)) # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # 7.499206349206349
print(miles_gallon_to_liters_100km(23.5)) # 10.009131205673757