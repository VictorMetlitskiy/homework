def oops():
    """Function causes an IndexError
    """
    raise IndexError


def catch_oops():
    """Function catches an IndexError and KeyError
    """
    try:
        oops()
    except IndexError:
        print('IndexError occurred.')
    except KeyError:
        print('KeyError occurred.')


catch_oops()
