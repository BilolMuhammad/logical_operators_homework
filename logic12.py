def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a // 10
    y = a % 10
    return a >= 10 and a <= 99 and x == y


print(main(39))
