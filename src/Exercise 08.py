from typing import List
from pathlib import Path

# __file__ is a string containing the path to this script's file. It is turned
# into a pathlib.Path so that the parent directory path can be retrieved with
# .parent.
root: Path = Path(__file__).parent

with open(Path(root, "GirlNames.txt")) as file:
    # Reads the file until EOF as one string and splits it into a list of lines.
    # This is done to remove the newline character.
    girls: List[str] = file.read().lower().splitlines()

with open(Path(root, "BoyNames.txt")) as file:
    # Reads the file until EOF as one string and splits it into a list of lines.
    # This is done to remove the newline character.
    boys: List[str] = file.read().lower().splitlines()

boy: str = input("Enter a boy's name or press [ENTER] to skip: ").lower()
girl: str = input("Enter a boy's name or press [ENTER] to skip: ").lower()

# Checks if the names given are not empty. If not, checks if they are in the
# respective lists.
if boy and boy in boys:
    print("The boy's name is among the most popular.")

if girl and girl in girls:
    print("The girls's name is among the most popular.")
