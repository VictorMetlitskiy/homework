# Task 3. Use a list comprehension to make a list containing tuples (i, j),
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
lst_tuples = [(num, num ** 2) for num in range(1, 11)]
print(lst_tuples)
