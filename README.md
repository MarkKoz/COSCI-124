# CO SCI 124 - Midterm
**Course Title:** Python Programming<br/>
**Section:** 28314<br/>
**Instructor:** Mohamad Pashazadeh Monajem<br/>
**Semester:** Fall 2017 (2017-08-28 to 2017-12-17)<br/>
**Textbook:** [Gaddis, Tony. _Starting out with Python_. 3rd ed.](http://www.mypearsonstore.com/bookstore/starting-out-with-python-subscription-0133743691)
(ISBN-13: 978-0-13-374369-2)

### Chapter 04
#### Exercise 11 - Calculating the Factorial of a Number
In mathematics, the notation `n!` represents the factorial of the nonnegative
integer `n`. The factorial of `n` is the product of all the nonnegative integers
from 1 to `n`. For example,

<p align="center"><code>7! = 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5,040</code></p>
and
<p align="center"><code>4! = 1 × 2 × 3 × 4 = 24</code></p>

Write a program that lets the user enter a nonnegative integer and then uses a
loop to calculate the factorial of that number. Display the factorial.

#### Exercise 14 - Write a program that uses nested loops to draw this pattern:
```
##
# #
#  #
#   #
#    #
#     #
```

### Chapter 05
#### Exercise 17 - Prime Numbers
A prime number is a number that is only evenly divisible by itself and 1. For
example, the number 5 is prime because it can only be evenly divided by 1 and 5.
The number 6, however, is not prime because it can be divided evenly by 1, 2, 3,
and 6. Write a Boolean function named `is_prime` which takes an integer as an
argument and returns true if the argument is a prime number, or false otherwise.
Use the function in a program that prompts the user to enter a number and then
displays a message indicating whether the number is prime.

> **TIP**: Recall that the  `%` operator divides one number by another and
returns the  remainder of the division. In an expression such as `num1 % num2`,
the `%` operator  will return `0` if `num1` is evenly divisible by `num2`.

#### Exercise 19 - Future Value
Suppose you have a certain amount of money in a savings account that earns
compound monthly interest, and you want to calculate the amount that you will
have after a specific number of months. The formula is as follows:

<p align="center"><code>F = P × (1 + i)<sup>t</sup></code></p>

The terms in the formula are:
* `F` is the future value of the account after the specified time period.
* `P` is the present value of the account.
* `i` is the monthly interest rate.
* `t` is the number of months.

Write a program that prompts the user to enter the account’s present value,
monthly interest rate, and the number of months that the money will be left in
the account. The program should pass these values to a function that returns the
future value of the account, after the specified number of months. The program
should display the account’s future value.

### Chapter 06
#### Exercise 07 -  Random Number File Writer
Write a program that writes a series of random numbers to a file. Each random
number should be in the range of 1 through 500. The application should let the
user specify how many random numbers the file will hold.

#### Exercise 08 - Random Number File Reader
This exercise assumes you have completed Programming Exercise 7, *Random Number
File Writer*. Write another program that reads the random numbers from the file,
display the numbers, and then display the following data:

* The total of the numbers
* The number of random numbers read from the file
