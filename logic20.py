def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.

    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x = n % 10
    return x > 0
