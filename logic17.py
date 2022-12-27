def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b1 = a % 10000
    b2 = b1 % 1000
    b3 = b2 % 100

    a1 = a // 10000
    a2 = b1 // 1000
    a3 = b2 // 100
    a4 = b3 // 10
    a5 = b3 % 10
    return a >= 10000 and a <= 99999 and a1 < a2 < a3 < a4 < a5 and a5 > a4 > a3 > a2 > a1


print(main(56789))
