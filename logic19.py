def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    n = x
    x1 = x % 10
    x //= 10
    x2 = x % 10
    x //= 10
    x3 = x % 10
    return x1 == x3 or (x1 == x2 and n < 99)


print(main(343))
