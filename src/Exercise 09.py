from typing import List
from pathlib import Path

# __file__ is a string containing the path to this script's file. It is turned
# into a pathlib.Path so that the parent directory path can be retrieved with
# .parent. Then the parent path is joined with the name of the data file. The
# result is a path to the data file which is located in the same directory as
# this script.
path: Path = Path(Path(__file__).parent, "USPopulation.txt")

# with statement automatically closes the file.
with open(path) as file:
    # Reads the file until EOF as one string and splits it into a list of lines.
    # This is done to remove the newline character.
    lines: List[str] = file.read().splitlines()

    # map() is used to cast each line in the list to an int. It returns an
    # iterator which is made into a list.
    populations: List[int] = list(map(int, lines))

# map() is used to apply a function to each element in the list. It returns an
# iterator which is made into a list.
# The lambda calculates the population change between the current year and the
# previous year.
# The populations list is sliced, removing the first year because the previous
# year's population is unknown.
changes = list(map((lambda p: p - populations[populations.index(p) - 1]),
               populations[1:]))

print(f"Average annual change: {int(sum(changes) / len(changes))}")

# Gets the index of the maximum value and adds to it 1951 (because index 0 is
# for year 1951).
print(f"Year with greatest increase: {changes.index(max(changes)) + 1951}")

# Gets the index of the minimum value and adds to it 1951 (because index 0 is
# for year 1951).
print(f"Year with smallest increase: {changes.index(min(changes)) + 1951}")
