def create_answer(name, day):    # Function for task 1.
    # Creating answer using f-string.
    string1 = f'Good day, {name}! {day} is perfect day to learn some Python.'
    # Creating answer using string format method.
    string2 = 'Good day, {}! {} is perfect day to learn some Python.'.format(name, day)
    # Creating answer using string concatenation.
    string3 = 'Good day, ' + name + '! ' + day + ' is perfect day to learn some Python.'
    return string1, string2, string3


def create_greeting(name, surname):    # Function for task 2
    # Create greeting using string concatenation
    string1 = 'Hello ' + name + ' ' + surname + '! Have a nice day.'
    # Create greeting using f-string
    string2 = f'Hello {name} {surname}! Have a nice day.'
    return string1, string2


def calculation(digit1, digit2):    # Function for task 3.
    string1 = f'{digit1} + {digit2} = {digit1 + digit2}'
    string2 = f'{digit1} - {digit2} = {digit1 - digit2}'
    string3 = f'{digit1} / {digit2} = {digit1 / digit2}'
    string4 = f' {digit1} * {digit2} = {digit1 * digit2}'
    string5 = f'{digit1} to the power of {digit2} = {digit1 ** digit2}'
    string6 = f'Module {digit1} = {abs(digit1)}'
    string7 = f'{digit1}//{digit2} = {digit1 // digit2}'
    return string1, string2, string3, string4, string5, string6, string7


day = 'Saturday'
name = 'Victor'
surname = 'Metlitskiy'
digit1 = 10
digit2 = 3

if __name__ == '__main__':
    string1, string2, string3 = create_answer(name, day)
    print(string1)
    print(string2)
    print(string3)
    print()
    string1, string2 = create_greeting(name, surname)
    print(string1)
    print(string2)
    print()
    string1, string2, string3, string4, string5, string6, string7 = calculation(digit1, digit2)
    print(string1)
    print(string2)
    print(string3)
    print(string4)
    print(string5)
    print(string6)
    print(string7)