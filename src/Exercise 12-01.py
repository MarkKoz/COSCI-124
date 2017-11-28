def main():
 #
 number = 0

 #
 number = int(input('How many numbers to display? '))

 #
 print_num(number)

#
def print_num(n):
    if n > 1:
        print_num(n - 1)
    print (n, sep=' ')

#
main()
