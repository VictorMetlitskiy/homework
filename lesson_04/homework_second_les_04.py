# Task 1.
string = input()
if len(string) >= 2:
    print(string[:2] + string[-2:])
else:
    print('Empty String')

# Task 2.
phone_number = input()
if phone_number.isdigit() and len(phone_number) == 10:
    print('Phone number is valid')
else:
    print('Phone number is invalid')

# Task 3.
name = 'victor'
my_name = input('Whire, please, your name: ')
if my_name.lower() == name:
    print('Your name is True')
else:
    print('Your name is False')