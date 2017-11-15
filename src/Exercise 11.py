import re

inp: str = input("Enter a string: ")

# Finds all matches of the pattern. The pattern matches any uppercase character
# followed by zero or more of any character other than an uppercase one.
# Concatenates the matches into a space-delimited string.
out: str = " ".join(re.findall(r"[A-Z][^A-Z]*", inp))

# # Ensures only the first character is capitalised.
out = out[0] + out[1:].lower()

print(out)
