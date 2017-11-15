from typing import List
from itertools import groupby

inp: str = input("Enter a string: ")

# Splits by upper-case characters. Converts iterator to a string with join().
groups: List[str] = [''.join(g[1]) for g in groupby(inp, str.isupper)]

# Merges every two groups in the list into one string. Done by zipping two
# subsets from groups which contain every second element, one starting at index
# 0 and the other at index 1.
# Then concatenates every word into a space delimited string.
out: str = ' '.join(''.join(c) for c in zip(groups[0::2], groups[1::2]))

# Ensures only the first character is capitalised.
out = out[0].upper() + out[1:].lower()

print(out)
