from typing import List

# Opens the file for reading.
with open("random.txt", "r") as f:
    # Reads the file as one string & splits lines by newline into a list.
    lines: List[str] = f.read().splitlines()

# Unpacks list of lines and prints them with a newline delimiter.
print(*lines, sep = "\n")

ints: List[int] = list(map(int, lines)) # Converts each lines from str to int.
total: int = sum(ints)  # Sum of all integers in the list.
length: int = len(ints) # Number of elements in the list.

print(f"Sum: {total}\nQuantity: {length}")

