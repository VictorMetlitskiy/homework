def oops():
    """Function causes an IndexError
    """
    raise IndexError('Index out of the range')


def catch_oops():
    """Function catches an IndexError and KeyError
    """
    try:
        oops()
    except IndexError as error:
        print(error)
    except KeyError:
        print('KeyError occurred.')


catch_oops()
