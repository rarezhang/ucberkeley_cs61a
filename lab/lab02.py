"""Required questions for lab 2"""
def welcome():
    print('welcome to')
    return 'hello'

def cs61a():
    print('cs61a')
    return 'world'
    
print(welcome(),cs61a())

## Boolean Operators ##

# Q6
def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x > 0 and y > 0 

## while Loops ##

# Q9
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i >= 1:
        if n % i == 0:
            print(i)
        i -= 1

# Q10
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    """
    "*** YOUR CODE HERE ***"
    first, second = 0,1
    while n != 0:
        first, second = second, first+second
        n -= 1
    return first
        

