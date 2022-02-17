def make_operation(operator, *args):
    """Performs operations on numbers depending on the passed operand and numbers.
    """
    subtraction_result = args[0]
    multiplication_result = 1

    if operator == '+':
        return sum(args)
    if operator == '-':
        for i in range(1, len(args)):
            subtraction_result -= args[i]
        return subtraction_result
    if operator == '*':
        for elem in args:
            multiplication_result *= elem
        return multiplication_result


if __name__ == '__main__':
    print(make_operation('-', 5, 5, -10, -20))
