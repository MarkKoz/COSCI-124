from typing import Dict

# Retrieves the user's input and stores as a string.
inp: str = input("Enter an integer within the range [1,10]: ")

# Retrieves the user's input until it consists of numeric characters.
while not inp.isdigit():
    inp = input("The input does not consist of numeric characters or is empty, "
                "try again: ")

# Retrieves the user's input until it is within the range [1,10].
while not 1 <= int(inp) <= 10:
    inp = input("The input is not within the range [1,10], try again: ")

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

i: int = int(inp) # Converts the input to an int.
print(f"The roman numeral equivalent of '{i}' is '{roman[i]}'.")
