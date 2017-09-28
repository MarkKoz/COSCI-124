total: int = 0 # Cumulative total of all inputs.
inp: int = int(input("Enter a positive number to continue "
                     "or a negative to stop: "))

# Prompts for a new input while the previous input is not negative.
while inp >= 0:
    total += inp # Adds the previous input to the total.
    inp = int(input("Enter a positive number to continue "
                    "or a negative to stop: "))

print(f"Total: {total}")
