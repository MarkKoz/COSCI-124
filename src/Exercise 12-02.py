def main():
    #
    num1 = 0
    num2 = 0

    #
    while num1 <= 0:
        num1 = int(input('Enter the first number: '))

    #
    while num2 <= 0:
        num2 = int(input('Enter the second number: '))

    #
    print(num1, 'times', num2, 'is', multiply(num1, num2))

#
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

#
main()
