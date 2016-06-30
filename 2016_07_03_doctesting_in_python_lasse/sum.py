def sum(*args):
    """
    Sums up all the arguments.

    >>> sum(1, 2, 3)
    6
    """
    return args[0] + sum(*args[1:]) if len(args) > 0 else 0
