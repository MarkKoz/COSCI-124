from typing import List
from pathlib import Path

# __file__ is a string containing the path to this script's file. It is turned
# into a pathlib.Path so that the parent directory path can be retrieved with
# .parent. Then the parent path is joined with the name of the data file. The
# result is a path to the data file which is located in the same directory as
# this script.
path: Path = Path(Path(__file__).parent, "numbers.txt")

try:
    file = open(path)
except IOError:
    print(f"There was a problem opening the file at {path}")
else:
    with file: # with statement automatically closes the file.
        # Reads the file until EOF as one string and splits it into a list of
        # lines. This is done to remove the newline character.
        lines: List[str] = file.read().splitlines()

        try:
            # map() is used to cast each line in the list to an int. It returns
            # an iterator which is made into a list.
            nums: List[int] = list(map(int, lines))

            # Sum of all values in the list divided by the total amount of
            # numbers.
            avg: float = sum(nums) / len(nums)
            print(avg)
        except ValueError as e:
            # Catches the exception thrown when casting str to int in map().
            # args[0] contains the exception message.
            print(e.args[0])
