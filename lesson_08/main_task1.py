def euclidean_gcd(num_a: int, num_b: int) -> int:
    """Function find the greatest common divisor num_a and num_b.
    """
    if not isinstance(num_a, int) or not isinstance(num_b, int):
        raise TypeError
    while num_a != num_b:
        if num_a > num_b:
            num_a = num_a - num_b
        elif num_b > num_a:
            num_b = num_b - num_a
    else:
        return num_a


if __name__ == '__main__':
    num1, num2 = 50, 45
    print(euclidean_gcd(num1, num2))
