from random import randint, sample

# Task 1.
number = randint(1, 10)

while True:
    user_number = input('Guess a number from 1 to 10: ')
    if not user_number.isdigit():
        continue
    elif int(user_number) > number:
        print(f'Guess number is less that {user_number}')
        continue
    elif int(user_number) < number:
        print(f'Guess number is greater than {user_number}')
        continue
    else:
        print(f'Guess number is {user_number}. You are the winner')
        break


# Task 2.
name = input('Write your name, please: ')

while True:
    age = input('Write you age, please (digit form): ')
    if not age.isdigit():
        continue
    else:
        print(f'Hello {name}, on your next birthday you’ll be {int(age)+1} years')
        break


# Task 3.
text = input('Write your string, please: ')
counter = 0
while counter < 5:
    lst_chars = sample(text, len(text))
    new_string = ''.join(lst_chars)
    print(new_string)
    counter += 1


# Task 4.
math_expression = input('Write answer, please, for expression 15 * 11 = ')
if math_expression == '165':
    print('Right answer')
else:
    print('Wrong answer')