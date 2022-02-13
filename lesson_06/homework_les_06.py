from random import randint


# Task 1.
# Creation list of 10 random numbers.
counter_num = 0
lst_num = list()
while counter_num < 10:
    random_number = randint(1, 1000)
    if random_number not in lst_num:
        lst_num.append(random_number)
        counter_num += 1

# Finding maximum number of list with while loop.
index_num = 1
max_number = lst_num[0]
while index_num <= 9:
    if lst_num[index_num] > max_number:
        max_number = lst_num[index_num]
    index_num += 1
print(max_number)

# Finding maximum number of list with built-in function max().
print(max(lst_num))

# Task 2.
counter_num = 0
lst_num1 = list()
lst_num2 = []
lst_num3 = []

while counter_num < 10:
    random_number = randint(1, 10)
    lst_num1.append(random_number)
    random_number = randint(1, 10)
    lst_num2.append(random_number)
    counter_num += 1

# Finding intersection through method 'intersection'.
set_num = set(lst_num1).intersection(set(lst_num2))
print(list(set_num))

# Finding intersection through operator '&'.
set_num2 = set(lst_num1) & (set(lst_num2))
print(list(set_num2))

# Finding an intersection using two for loops.
# Content matching is guaranteed, order is not.
for elem1 in lst_num1:
    for elem2 in lst_num2:
        if elem1 == elem2 and elem1 not in lst_num3:
            lst_num3.append(elem1)
print(lst_num3)

# Task 3.
list_num = list(range(1, 101))
list_num2 = []
index_num = 0

while index_num < 100:
    if list_num[index_num] % 7 == 0 and list_num[index_num] % 5 != 0:
        list_num2.append(list_num[index_num])
    index_num += 1
print(list_num2)

# Additional task. Creation game 'Minesweeper'.


# Define function for printing grid.
def print_grid(matrix):
    for raw in grid:
        for elem in raw:
            print(elem, end=' ')
        print()


# Define function for playing game.
def play_game():
    counter_mines = 0
    counter = 1
    while counter_mines < 10:
        row_x = input(f'Attempt {counter}. Write first coordinate x from 1 to 8 or enter exit/e/- for cancel game: ')
        if row_x.lower() in ['exit', 'e', '-']:
            return counter_mines
        elif row_x.isdigit() and 1 <= int(row_x) <= 8 and '*' in grid_for_user[int(row_x)-1]:
            while True:
                column_y = input(f'Attempt {counter}. Write second coordinate y from 1 to 8 or enter exit/e/- \
for cancel game: : ')
                if column_y.lower() in ['exit', 'e', '-']:
                    return counter_mines
                elif column_y.isdigit() and 1 <= int(column_y) <= 8 and \
                        str(grid_for_user[int(row_x)-1][int(column_y)-1]) not in 'XO':
                    break
                else:
                    continue
        else:
            continue
        row_x = int(row_x)-1
        column_y = int(column_y)-1
        if grid[row_x][column_y] == 'M':
            grid_for_user[row_x][column_y] = 'X'
            counter_mines += 1
            print_grid(grid_for_user)
            if counter_mines < 10:
                print(f'You have guessed! {10 - counter_mines} mine(s) left to find!')
            else:
                return counter_mines
        else:
            grid_for_user[row_x][column_y] = 'O'
            print_grid(grid_for_user)
            print(f'Failed! {10 - counter_mines} mine(s) left to find!')
        counter += 1


count_game = 0
while True:
    if count_game == 0:
        print('Do you want to play the game of Minesweeper?')
    else:
        print('Do you want to play the game of Minesweeper again?')
    answer = input('Write, please, y/n or +/- ')
    if answer.lower() not in ['yes', 'y', '+', 'no', 'n', '-']:
        continue
    elif answer.lower() in ['yes', 'y', '+']:
        grid = [['*'] * 8 for _ in range(8)]
        grid_for_user = [['*'] * 8 for _ in range(8)]
        counter_insert_mines = 0
        while counter_insert_mines < 10:
            row_index = randint(0, 7)
            column_index = randint(0, 7)
            if grid[row_index][column_index] == '*':
                grid[row_index][column_index] = 'M'
                counter_insert_mines += 1
        counter_find_mines = play_game()
        count_game += 1
        if counter_find_mines == 10:
            print(f'Congratulation! I have found all mines. You played the game {count_game} time(s)')
        else:
            print(f"You played the game {count_game} time(s). Let's play next time ;)")
            break
    else:
        print("Let's play next time.")
        break
