def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = a % 100
    x = a // 100
    y = b // 10
    z = b % 10
    return a >= 100 and a <= 999 and (x+y+z) % 2 != 0


print(main(124))
