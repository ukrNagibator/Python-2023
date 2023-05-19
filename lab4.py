import time
import random
#TASK 1
n = int(input("Enter a number: "))
print(n >= 100)

''' TASK 2

if n > m:
    print("First number > Second")
elif n < m:
    print("First number < Second")
else:
    print("First number = Second") '''

#task 3
flower = input("Enter flower name: ")

if (flower == 'Spathiphyllum'):
    print("“Yes - Spathiphyllum is the best plant ever!”")
elif(flower == "spathiphyllum"):
    print('No, I want a big Spathiphyllum!')
else:
    print('Spathiphyllum! Not' + flower + '!')


#task 4
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = round(income * 0.18 - 556.02)
else:
    tax = round(14839.02 + 0.32 * (income - 85528))

if tax < 0:
    tax = 0
print(f"Tax is: {tax:.1f} tallers")


#task 5
year = int(input("enter year: "))
if year <=1581:
    print("Not within the Gregorian calendar period.")
elif year % 4 != 0:
    print(year, " - common year")
elif year % 100 != 0:
    print(year, " - leap year")
elif year % 400 != 0:
    print(year, " - common year")
else:
    print(year, " - leap year")

#task 6
while user_number != secret_number:
    user_number = int(input("enter 4 symbols number: "))
    if user_number > 9999 or user_number < 1000:
        print("not 4 symbols number .")
    elif user_number != secret_number:
        print("Ха-ха! Ви застрягли у моїй петлі!")
    else:
        print("Молодець, магле! Тепер ти вільний!")


#task 7
i = 1
while i <= 5:
    print(str(i) + ' Mississippi')
    time.sleep(1)
    i+=1
else:
    print('Ready or not, here i come!')
#task 8
    something = str(input("Enter the secret word: "))
    while True:
        if something == 'chupacabra':
            print('You successfully left the loop')
            break
        else:
            print("Secret word still not guessed")

#task 9
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    print(letter)


    #task 10

word_without_vowels = ""

user_word = input("Введіть слово: ")
word_without_vowels = ""

for letter in user_word.upper():
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    else:
        word_without_vowels += letter

print("Рядок без голосних:", word_without_vowels)
# Print the word assigned to word_without_vowels.


#TASK 11
blocks = int(input("Введіть кількість блоків: "))
height = 0
layer_blocks = 1

while True:
    if blocks < layer_blocks:
        break
    height += 1
    blocks -= layer_blocks
    layer_blocks += 1