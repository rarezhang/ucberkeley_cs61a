def my_email():
    """Return your email address as a string.

    >>> my_email() != 'oski@berkeley.edu'
    True
    """
    return 'wenli@berkeley.edu'

from operator import add, mul

def twenty_fifteen():
    """Come up with the most creative expression that evaluates to 2015,
    using only numbers and the functions add(. . .) and mul(. . .).

    >>> twenty_fifteen()
    2015
    """
    "*** YOUR CODE HERE ***"
    return add(mul(10,200),mul(3,5))
