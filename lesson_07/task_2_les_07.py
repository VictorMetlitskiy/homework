# Task 2.


def compute_total_price(dict_quantity, dict_price):
    lst_total_price = [dict_quantity[key] * dict_price[key] for key in dict_quantity]
    return sum(lst_total_price)


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = compute_total_price(stock, prices)
print(total_price)