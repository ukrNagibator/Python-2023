#1 task
""" Ваше завдання:

напишіть рядок коду, що пропонує користувачеві замінити число всередині списку цілим числом, введеним користувачем (крок 1)
напишіть рядок коду, який видаляє останній елемент зі списку (крок 2)
напишіть рядок коду, який друкує довжину існуючого списку (крок 3)."""
hat_list = [1, 2, 3, 4, 5]

print('You got a list with: \n')
print(hat_list)
print('Enter the number which will replace: ')
new_number = int(input("Введите новое число: "))
index = 2
hat_list[index] = new_number
del hat_list[4]
print(hat_list)
print(len(hat_list))

#2 task
"""Написати програму сортування списку у порядку зростання методом бульбашки."""
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [1000, 5, 3, 4, 2, 0, 1, 991, 22232, 323232, 232323232, 3232323232323]
sorted_lst = bubble_sort(lst)
print(sorted_lst)

#3 task
"""Уявіть список - не дуже довгий, не дуже складний, просто звичайний список, що містить деякі цілі числа. Деякі з цих чисел можуть повторюватись, і це ключ до розгадки. Ми не хочемо повторень. Ми хочемо, щоб їх видалили.

Ваше завдання – написати програму, яка видаляє всі дублікати чисел зі списку. Ціль полягає в тому, щоб скласти список, в якому всі числа зустрічаються не більше одного разу.

Примітка: припустимо, що вихідний список жорстко закодований всередині коду - Вам не потрібно вводити його з клавіатури. Звичайно, Ви можете покращити код і додати частину, яка може вести діалог з користувачем і отримувати від неї всі дані.

Підказка: ми рекомендуємо Вам створити новий список як тимчасову робочу область - вам не потрібно оновлювати список in situ.

Ми не надали тестових даних, оскільки було б надто просто. Натомість ви можете використовувати наш скелет."""

numbers = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_numbers = []
for num in numbers:
    if num not in new_numbers:
        new_numbers.append(num)

print(new_numbers)

#4 task
"""Напишіть код, використоувуючи генератори списків, який створює матрицю 8х8 з пустими клітинками (пуста клітинка задається як “_“) для задання шахівниці і розставте чотири тури по кутках шахівниці"""
board = [["_"] * 8 for _ in range(8)]

board[0][0] = "R"
board[0][7] = "R"
board[7][0] = "R"
board[7][7] = "R"

for row in board:
    print(" ".join(row))