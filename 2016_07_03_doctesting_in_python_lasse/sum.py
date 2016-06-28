def sum(*args):
    """
    Sums up all the arguments.

    >>> sum(1, 2, 3)
    6
    """
    result = 0
    for arg in args: result += arg

