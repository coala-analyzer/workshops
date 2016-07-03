def sum(*args):
    """
    Sums up all the arguments:

    >>> sum(1, 2.5, 3)
    6.5

    If you don’t provide any arguments, it’ll return 0:

    >>> sum()
    0

    :param args: Any numbers to sum up.
    :return:     The sum of all the given
    """
    return args[0] + sum(*args[1:]) if len(args) > 0 else 0
