# Task 1.
weight = 82
height = 1.74
IBM = weight / (height * height)
print(f'Your BMI is normal: {18.5 < IBM < 25}')

# Task 2.
valid_number = input()
check1 = len(valid_number) == 12
check2 = valid_number.isdigit()
check3 = valid_number.startswith('380')
total = check1 + check2 + check3
print(f'This number is valid: {total == 3}')