from typing import List

total: int = 20 # Number of questions in the exam.
scorePass: int = 15 # Number of correct questions required to pass the exam.

answers: List[str] = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A",
                      "D", "C", "A", "D", "C", "B", "B", "D", "A"]

# Creates a text file and writes the answers to it.
with open("answers.txt", "w") as file:
    # Creates a newline-delimited string of answers and writes it to the file.
    file.write("\n".join(answers))

# Assumes all question are answered i.e 20 lines will be read in total.
with open("exam.txt") as file:
    # Reads the file until EOF as one string and splits it into a list of lines.
    # This is done to remove the newline character.
    exam: List[str] = file.read().splitlines()

incorrect: List[int] = [] # A list of questions which were answered incorrectly.

# Iterates in parallel over the student's answers and the answer key using
# zip(). Uses enumerate() to create a counter, i, starting at 1. Appends the
# question number, i, to incorrect if the current student's answer and the
# answer in the key are not equal.
for i, (e, a) in enumerate(zip(exam, answers), 1):
    if e != a:
        incorrect.append(i)

totalInc: int = len(incorrect) # Number of incorrect answers.

if totalInc > total - scorePass:
    print("Failed.")
else:
    print("Passed.")

print(f"Correct: {total - totalInc}")
print(f"Incorrect: {totalInc}")
print(", ".join(map(str, incorrect)))
