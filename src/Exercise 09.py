from typing import FrozenSet

vowels: FrozenSet[str] = frozenset("aeiou")
consonants: FrozenSet[str] = frozenset("bcdfghjklmnpqrstvwxyz")

def countChars(s: str, chars: FrozenSet[str]) -> int:
    """
    Counts the number of characters from the set :any:`c` present in string `s`.

    Parameters
    ----------
    s: str
        The string the characters of which are to be counted.

    chars: FrozenSet[str]
        A set of which characters to count.

    Returns
    -------
    int
        The count of characters.

    """
    return sum(s.count(c) for c in chars)

inp: str = input("Enter a string: ").lower()

print(f"Vowels: {countChars(inp, vowels)}")
print(f"Consonants: {countChars(inp, consonants)}")
