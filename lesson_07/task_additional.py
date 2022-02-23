from operator import itemgetter

# 1. Sort list of dicts by key ‘type’.
# 2. Sort list of dicts by value of key ‘year’.
vehicles = [
    {'type': 'Sedan', 'weight': 1500, 'year': 2000},
    {'type': 'SUV', 'weight': 2000, 'year': 1999},
    {'type': 'Pickup', 'weight': 2500, 'year': 2011},
    {'type': 'Minivan', 'weight': 1600, 'year': 1999},
    {'type': 'Van', 'weight': 2400, 'year': 2012},
    {'type': 'Semi', 'weight': 13600, 'year': 2015},
    {'type': 'bycycle', 'weight': 7, 'year': 2012},
    {'type': 'Motorcycle', 'weight': 100, 'year': 2008}
]

# Sort list of dictionary by value of key 'year' using lambda function.
sorted_list = sorted(vehicles, key=lambda d: d['year'])
for elem in sorted_list:
    print(elem)
print()

# Sort list of dictionary by value of key 'type' using method itemgetter.
sorted_list = sorted(vehicles, key=itemgetter('type'))
for elem in sorted_list:
    print(elem)
print()

# Sort list of dictionary by key through lambda function. Compared data must be of the same type.
dict_unsorted = {'weight': 1500, 'code': 10000, 'year': 2000}
dict_sorted = {key: value for key, value in sorted(dict_unsorted.items(), key=lambda item: item[0])}
print(dict_sorted)

# Sort dictionary by value through itemgetter method. Compared data must be of the same type.
dict_sorted = {key: value for key, value in sorted(dict_unsorted.items(), key=itemgetter(1))}
print(dict_sorted)
