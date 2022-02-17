def make_country(country, capital):
    """Create the dict with country as key and capital as value.
    """
    dict_country = dict()
    dict_country[country] = capital
    return dict_country


if __name__ == '__main__':
    name_country = input('Write, please, name of country: ')
    name_capital = input('Write, please, capital of country: ')
    print(make_country(name_country, name_capital))
