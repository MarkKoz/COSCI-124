import locale

locale.setlocale(locale.LC_ALL, "en") # 'en': 'en_US.ISO8859-1'.
price: int = 99 # Base price of each package.

def getInput() -> int:
    """
    Retrieves the number of packages purchased from the user. Prompts for a new
    input if the one given is invalid.

    A valid input is one that:
    * Is not empty.
    * Consists only of digit characters (0-9).

    Returns
    -------
    int
        The input given representing the number of packages purchased.
    """
    # Retrieves the user's input and stores as a string.
    i: str = input("Enter the number of packages purchased: ")

    # Retrieves the user's input until it consists of numeric characters.
    while not i.isdigit():
        i = input("The input does not consist of numeric characters or is empty"
                  ", try again: ")

    return int(i)

def getDiscount(quantity: int) -> float:
    """
    Returns the discount for a given quantity.

    * 10-19 packages: 10% discount
    * 20-49 packages: 20% discount
    * 50-99 packages: 30% discount
    * 100+ packages: 40% discount

    Parameters
    ----------
    quantity: int
        The amount of packages purchased.

    Returns
    -------
    float
        The discount rate represented in decimal form.
    """
    if 10 <= quantity <= 19:
        return 0.1

    if 20 <= quantity <= 49:
        return 0.2

    if 50 <= quantity <= 99:
        return 0.3

    if quantity >= 100:
        return 0.4

    return 0

quant: int = getInput() # Number of packages purchased.
discount: float = getDiscount(quant) # Discount rate.
gross: float = quant * price # Gross total, before applying discount.
savings: float = gross * discount # Amount of money to deduct due to discount.

print(f"Discount rate: {int(discount * 100)}%")
print(f"Savings: {locale.currency(savings, grouping = True)}")
print(f"Net total: {locale.currency(gross - savings, grouping = True)}")
