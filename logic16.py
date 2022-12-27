def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a >= 10000 and a <= 99999 and a % (a//1) == 0


print(main(11178.5))
