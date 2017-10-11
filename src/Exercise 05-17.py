def is_prime(i: int) -> bool:
    """
    Performs a primality test on :any:`i` using trial division.

    Parameters
    ----------
    i: int
        The integer on which to perform the primality test.

    Returns
    -------
    bool
        True if :any:`i` is prime; False otherwise.
    """
    # Goes first so that the modulo operation which follows doesn't falsely
    # return false. 2 is the only even prime.
    if i == 2:
        return True

    # 2 is the smallest prime, so anything lesser is not. Anything not evenly
    # divisible by 2 also is not prime.
    if i < 2 or i % 2 == 0:
        return False

    # The square root is calculated using the power operator because it seems
    # to be significantly faster in this case.
    #
    # Square root is convert to an int, which truncates the decimals. Then, 1 is
    # added effectively doing math.ceil() except the end result is an int, not a
    # float.
    #
    # Iterates from 3 to the square root (1 is added because range() is
    # exclusive of the end.) Starts at 3 because i % 2 is already performed
    # earlier. Ends at the square root because one factor must always be equal
    # to or less than the square root, therefore a guarantee of finding a factor
    # if i isn't prime.
    #
    # The step is 2 because all even numbers have have already been eliminated
    # and odd % even will never evaluate to 0.
    #
    # Use modulo to determine i is evenly divisible by any number in the range,
    # which would mean it is a factor and thus i isn't prime. If the modulo
    # expression evaluates to True in any iteration, it means a factor was
    # found. If not, it means i is prime. Thus, the the return of any() is
    # negated and returned.
    return not any(i % x == 0 for x in range(3, int(i ** 0.5) + 2, 2))

num: int = int(input("Enter an integer on which to perform a primality test: "))
print(f"{num} is prime: {is_prime(num)}")
