import random
import time


blocks = int(input("Введіть кількість блоків: "))
height = 0
layer_blocks = 1

while True:
    if blocks < layer_blocks:
        break
    height += 1
    blocks -= layer_blocks
    layer_blocks += 1

print("Висота піраміди:", height)


i = 1
while i <= 5:
    print(str(i) + ' Mississippi')
    time.sleep(1)
    i+=1
else:
    print('Ready or not, here i come!')


something = str(input("Enter the secret word: "))
while True:
    if something == 'chupacabra':
        print('You successfully left the loop')
        break
    else:
        print("Secret word still not guessed")
        break

    secret_number = random.randrange(1000, 10000)
    user_number = 0

    for i in range(2, 8, 3):
        print("The value of i is currently", i)

    while user_number != secret_number:
        user_number = int(input("enter 4 symbols number: "))
        if user_number > 9999 or user_number < 1000:
            print("not 4 symbols number .")
        elif user_number != secret_number:
            print("Ха-ха! Ви застрягли у моїй петлі!")
        else:
            print("Молодець, магле! Тепер ти вільний!")