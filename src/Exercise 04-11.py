def getInput() -> int:
    """
    Prompts the user to input a non-negative integer.

    Returns
    -------
    int
        Thee user's input.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0: return num
            print("Input is negative, try again.")
        except ValueError:
            print("Input is not an integer, try again.")

def calcFactorial(n: int) -> int:
    """
    Calculates the factorial of :any:`n`. The factorial is the product of all
    positive integers less than or equal to :any:`n`.

    Notes
    -----
    :math:`0! = 1`

    Parameters
    ----------
    n: int
        A non-negative integer for which to calculate the factorial.
    Returns
    -------
    int
        The product of the factorial operation.
    """
    product: int = 1  # The product of the factorial operation.

    while n > 0:
        product *= n
        n -= 1

    return product

num: int = getInput()
print(f"{num}! = {calcFactorial(num)}")
