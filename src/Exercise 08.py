def capitalise(s: str) -> str:
    """
    Returns a string :any:`s` with the first letter of every word capitalised.
    Word boundaries are defined by whitespaces.

    Parameters
    ----------
    s: str
        The string to capitalise.

    Returns
    -------
    str
        The capitalised string.
    """
    # splits the string into words by whitespace.
    # Capitalises the first letter and concatenates it with the rest of the
    # word.
    # Each word is concatenated with join(), being delimited by a whitespace.
    return " ".join(w[0].upper() + w[1:] for w in s.split())

inp: str = input("Enter a string to capitalise: ")
print(capitalise(inp))
