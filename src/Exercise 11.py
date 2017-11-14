from typing import List
import itertools

def validate(square: List[List[int]]) -> bool:
    """
    Determines if a square matrix :any:`square` is a Lo Shu Magic Square. The
    criteria for a valid Lo Shu Magic Square is:

    * The grid contains the numbers 1 through 9 exactly.
    * The sum of each row, each column, and each diagonal all add up to the same
      number.

    Parameters
    ----------
    square: List[List[int]]
        A 2-dimensional list of integers representing a square matrix which will
        be validated.

    Returns
    -------
    bool
        True if :any:`square` is a Lo Shu Magic Square; False otherwise.
    """
    # Flattens the matrix into one dimension.
    flat: List[int] = list(itertools.chain.from_iterable(square))

    # Checks if elements are in the range [1, 9].
    if any(i not in range(1, 10) for i in flat):
        return False

    # Checks if elements are unique by checking if the length changes when
    # converted to a set.
    if len(flat) != len(set(flat)):
        return False

    s: int = sum(square[0]) # Sum of rows, columns, and diagonals.

    # Checks rows, excluding the first row.
    if any(sum(row) != s for row in square[1:]):
        return False

    # Checks columns.
    # Assumes the matrix is a square i.e. column length = row length.
    if any(sum(row[col] for row in square) != s for col in range(len(sq))):
        return False

    # Checks principal diagonal.
    if sum(row[i] for i, row in enumerate(square)) != s:
        return False

    # Checks counter diagonal.
    if sum(row[~i] for i, row in enumerate(square)) != s:
        return False

    return True

sq: List[List[int]] = [[4, 9, 2],
                       [3, 5, 7],
                       [8, 1, 6]]

print("Valid.") if validate(sq) else print("Invalid.")
