def counter(start=1):
    """
    Generates increasing numbers beginning with your sta'rt, see:

    >>> counter()  # doctest: +ELLIPSIS
    <generator object counter at 0x...>
    """
    while True:
        yield start
        start += 1
