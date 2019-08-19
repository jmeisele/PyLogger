def add(x, y):
    """ Returns sum of x and y"""
    return x + y


def subtract(x, y):
    """ Returns different of x and y"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def division(x, y):
    """ Divide function"""
    if y == 0:
        raise ValueError('Cannot divide by 0!')
    return x / y
