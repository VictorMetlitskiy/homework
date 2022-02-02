# Use function print wiht different argements
numbers = 1, 2, 3, 4, 5, 6, 7
numbers1 = [num for num in range(10)]
s = 'Happy_Pythoning!'

if __name__ == '__main__':
# Output: Happy_Pythoning!
    print(s)
# Output: Happy_Pythoning!*Happy_Pythoning!Happy_Pythoning!Happy_Pythoning!
    print(s, s*3, sep='*', end='\n\n')
# Output: (1, 2, 3, 4, 5, 6, 7)
    print(numbers)
# Output: 0 1 2 3 4 5 6 7 8 9
    print(*numbers1)
# Output: H-a-p-p-y-_-P-y-t-h-o-n-i-n-g-!
    print('-'.join(s))