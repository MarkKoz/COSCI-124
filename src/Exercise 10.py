from typing import List

# with statement automatically closes the file.
with open("WorldSeriesWinners.txt") as file:
    # Reads the file until EOF as one string and splits it into a list of lines.
    # This is done to remove the newline character.
    winners: List[str] = file.read().lower().splitlines()

team = input("Enter a team's name: ")

print(f"{team} has won the World Series {winners.count(team.lower())} times.")
