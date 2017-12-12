def main():
    # Redundantly declares and initialises the variable to an "empty" value.
    number = 0

    # Variable is set to something useful - the user's input.
    number = int(input('How many numbers to display? '))

    # Calls the print_num function with the user's input as the argument.
    print_num(number)

# Recursively calls itself while the argument is greater than 1. One is
# subtracted from the argument for every recursive call. The result is numbers
# printed in ascending order up to the value of the argument (inclusive).
def print_num(n):
    if n > 1:
        print_num(n - 1)
    print(n, sep = ' ')

# Calls the main function when the program runs.
main()
