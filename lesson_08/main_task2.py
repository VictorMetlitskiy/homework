def nested_parentheses(string):
    """Function evaluates equality of parentheses.
    """
    number_parentheses = 0
    if len(string) == 0:
        return True
    for elem in string:
        if elem == '(':
            number_parentheses += 1
        elif elem == ')':
            number_parentheses -= 1
            if number_parentheses < 0:
                return False
        else:
            return False
    if number_parentheses == 0:
        return True


if __name__ == '__main__':
    parentheses = input('Write, please, text consisting of parentheses: ')
    print(f'{parentheses} = ', nested_parentheses(parentheses))
