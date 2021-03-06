# Define function for task 3
def draw_box():
    print('#'*9, '\n#\t\t#'*3, '\n', '#'*9, sep='')
    print()
    print('#\t\t#\n'*2, '#'*9, '\n#\t\t#'*2, sep='')


# Use function print wiht different argements
numbers = 1, 2, 3, 4, 5, 6, 7
lst_numbers = [num for num in range(10)]
text = 'Happy_Pythoning!'

if __name__ == '__main__':
# Output: Happy_Pythoning!
    print(text)
# Output: Happy_Pythoning!*Happy_Pythoning!Happy_Pythoning!Happy_Pythoning!
    print(text, text*3, sep='*', end='\n\n')
# Output: (1, 2, 3, 4, 5, 6, 7)
    print(numbers)
# Output: 0 1 2 3 4 5 6 7 8 9
    print(*lst_numbers)
# Output: H-a-p-p-y-_-P-y-t-h-o-n-i-n-g-!
    print('-'.join(text))
    print()
    draw_box()