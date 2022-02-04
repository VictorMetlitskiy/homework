def create_answer(name, day):    # Function for task 1.
    # Creating answer using f-string.
    s1 = f'Good day, {name}! {day} is perfect day to learn some Python.'
    # Creating answer using string format method.
    s2 = 'Good day, {}! {} is perfect day to learn some Python.'.format(name, day)
    # Creating answer using string concatenation.
    s3 = 'Good day, ' + name + '! ' + day + ' is perfect day to learn some Python.'
    return s1, s2, s3


def create_greeting(name, surname):    # Function for task 2
    # Create greeting using string concatenation
    s1 = 'Hello ' + name + ' ' + surname + '! Have a nice day.'
    # Create greeting using f-string
    s2 = f'Hello {name} {surname}! Have a nice day.'
    return s1, s2


def calculation(a, b):    # Function for task 3.
    s1 = f'{a} + {b} = {a + b}'
    s2 = f'{a} - {b} = {a - b}'
    s3 = f'{a} / {b} = {a / b}'
    s4 = f' {a} * {b} = {a * b}'
    s5 = f'{a} to the power of {b} = {a ** b}'
    s6 = f'Module {a} = {abs(a)}'
    s7 = f'{a}//{b} = {a // b}'
    return s1, s2, s3, s4, s5, s6, s7


day = 'Saturday'
name = 'Victor'
surname = 'Metlitskiy'
x = 10
y = 3

if __name__ == '__main__':
    s1, s2, s3 = create_answer(name, day)
    print(s1)
    print(s2)
    print(s3)
    print()
    s1, s2 = create_greeting(name, surname)
    print(s1)
    print(s2)
    print()
    s1, s2, s3, s4, s5, s6, s7 = calculation(x, y)
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print(s7)
