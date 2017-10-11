lines: int = 6 # Total number of lines in the pattern.
char: str = "#" # The character at either end of the line.
pad: str = " " # The character to use as padding between the ends.

# One iteration for every line
for l in range(lines):
    line: str = char # Adds the char to the start of the line.

    # One iteration for every padding character to insert.
    # Using mod makes the first line have no padding because 0 % x = 0.
    # range() being 0-based works in this program's favour here because the
    # amount of padding needs to be one less than the line number.
    for _ in range(l % lines):
        line += pad # Adds one padding character.

    line += char # Adds the char to the ends of the line.
    print(line) # Prints the completed line.

