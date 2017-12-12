def main():
    # Declares and initialises variables.
    num1 = 0
    num2 = 0

    # Retrieves user input until a number greater than 0 is entered.
    while num1 <= 0:
        num1 = int(input('Enter the first number: '))

    # Retrieves user input until a number greater than 0 is entered.
    while num2 <= 0:
        num2 = int(input('Enter the second number: '))

    # Prints the result of the multiply function with the two user inputs as
    # its arguments.
    print(num1, 'times', num2, 'is', multiply(num1, num2))

# Returns the product of multiplying the two arguments.
# Works recursively, returning the multiplicand plus the return value of the
# recursive call with the multiplier decremented by one. This effectively
# adds the multiplicand for multiplier number of times.
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

# Calls the main function when the program runs.
main()
