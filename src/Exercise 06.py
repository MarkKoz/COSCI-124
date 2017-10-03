from typing import List
from pathlib import Path

# __file__ is a string containing the path to this script's file. It is turned
# into a pathlib.Path so that the parent directory path can be retrieved with
# .parent. Then the parent path is joined with the name of the data file. The
# result is a path to the data file which is located in the same directory as
# this script.
path: Path = Path(Path(__file__).parent, "numbers.txt")

# with statement automatically closes the file.
with open(path) as file:
    # Reads the file until EOF as one string and splits it into a list of lines.
    # This is done to remove the newline character.
    lines: List[str] = file.read().splitlines()

    # map() is used to cast each line in the list to an int. It returns an
    # iterator which is made into a list.
    nums: List[int] = list(map(int, lines))

    # Sum of all values in the list divided by the total quantity of numbers.
    avg: float = sum(nums) / len(nums)
    print(avg)
