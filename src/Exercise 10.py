from collections import Counter

# Could add lower() here to make the count case-insensitive.
inp: str = input("Enter a string: ")

# Concatenates the first value of every tuple returned by most_common() into a
# comma-delimited list.
chars = ", ".join(c[0] for c in Counter(inp).most_common())
print(f"Most frequent character(s): {chars}")
