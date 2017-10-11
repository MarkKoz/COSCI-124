from random import randrange

capacity: int = int(input("Enter the capacity of the file: "))

# Opens the file for writing.
with open("random.txt", "w") as f:
    # One iteration for every line to write (determined by capacity).
    for _ in range(capacity):
        # Generates a random integer in the range [1,501).
        # Converts the integer to a string.
        # Writes the string to the file.
        f.write(str(randrange(1, 501)) + "\n")
