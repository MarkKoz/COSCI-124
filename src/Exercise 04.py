from typing import Dict

def getInput() -> int:
    """
    Prompts the user to enter an integer within the range [1,10]. If the input
    is invalid, an error is shows and the user is prompted for a new input.

    Returns
    -------
    int
        The user's input.
    """
    # Retrieves the user's input and stores as a string.
    i: str = input("Enter an integer within the range [1,10]: ")

    # Retrieves the user's input until it consists of numeric characters.
    while not i.isdigit():
        i = input("The input does not consist of numeric characters or is empty"
                  ", try again: ")

    # Retrieves the user's input until it is within the range [1,10].
    while not 1 <= int(i) <= 10:
        i = input("The input is not within the range [1,10], try again: ")

    return int(i)

# Associates integers with roman numerals.
roman: Dict[int, str] = {1: "I",
                         2: "II",
                         3: "III",
                         4: "IV",
                         5: "V",
                         6: "VI",
                         7: "VII",
                         8: "VIII",
                         9: "IX",
                         10: "X"}

inp: int = getInput()
print(f"The roman numeral equivalent of '{inp}' is '{roman[inp]}'.")
