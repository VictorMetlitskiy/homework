def operate_num():
    """Function take two numbers a and b via input() and returns value a**2/b
    """
    try:
        num1 = int(input('Type a first num: '))
        num2 = int(input('Type a second num: '))
        return num1**2/num2
    except ZeroDivisionError as err:
        print(err, 'second num must not be null')
    except ValueError as err:
        print(err, 'characters must be numbers')


function_value = operate_num()
