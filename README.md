# CO SCI 124 - Chapter 07: Programming Exercises
**Course Title:** Python Programming<br/>
**Section:** 28314<br/>
**Instructor:** Mohamad Pashazadeh Monajem<br/>
**Semester:** Fall 2017 (2017-08-28 to 2017-12-17)<br/>
**Textbook:** [Gaddis, Tony. _Starting out with Python_. 3rd ed.](http://www.mypearsonstore.com/bookstore/starting-out-with-python-subscription-0133743691)
(ISBN-13: 978-0-13-374369-2)

### Exercise 07 - Driver’s License Exam
The local driver’s license office has asked you to create an application that
grades the written portion of the driver’s license exam. The exam has 20
multiple-choice questions. Here are the correct answers:

1. A
2. C
3. A
4. A
5. D
6. B
7. C
8. A
9. C
10. B
11. A
12. D
13. C
14. A
15. D
16. C
17. B
18. B
19. D
20. A

Your program should store these correct answers in a list. The program should
read the student’s answers for each of the 20 questions from a text file and
store the answers in another list. (Create your own text file to test the
application.) After the student’s answers have been read from the file, the
program should display a message indicating whether the student passed or failed
the exam. (A student must correctly answer 15 of the 20 questions to pass the
exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the
question numbers of the incorrectly answered questions.

### Exercise 08 - Name Search
If you have downloaded the source code from this book’s companion Web site, you
will find the following files in the *Chapter 07* folder:

* `GirlNames.txt`—This file contains a list of the 200 most popular names given
to girls born in the United States from the year 2000 through 2009.
* `BoyNames.txt`—This file contains a list of the 200 most popular names given
to boys born in the United States from the year 2000 through 2009.

Write a program that reads the contents of the two files into two separate
lists. The user should be able to enter a boy’s name, a girl’s name, or both,
and the application will display messages indicating whether the names were
among the most popular.

(You can access the book’s companion Web site at
[www.pearsonglobaleditions.com/gaddis](www.pearsonglobaleditions.com/gaddis).)

### Exercise 09 - Population Data
If you have downloaded the source code from this book’s companion Web site, you
will find a file named `USPopulation.txt` in the *Chapter 07* folder. The file
contains the midyear population of the United States, in thousands, during the
years 1950 through 1990. The first line in the file contains the population for
1950, the second line contains the population for 1951, and so forth.

Write a program that reads the file’s contents into a list. The program should
display the following data:

* The average annual change in population during the time period
* The year with the greatest increase in population during the time period
* The year with the smallest increase in population during the time period

(You can access the book’s companion Web site at
[www.pearsonglobaleditions.com/gaddis](www.pearsonglobaleditions.com/gaddis).)

### Exercise 10 - World Series Champions
If you have downloaded the source code from this book’s companion Web site, you
will find a file named `WorldSeriesWinners.txt` in the *Chapter 07* folder. This
file contains a chronological list of the World Series winning teams from 1903
through 2009. (The first line in the file is the name of the team that won in
1903, and the last line is the name of the team that won in 2009. Note that the
World Series was not played in 1904 or 1994.)

Write a program that lets the user enter the name of a team and then displays
the number of times that team has won the World Series in the time period from
1903 through 2009.

(You can access the book’s companion Web site at
[www.pearsonglobaleditions.com/gaddis](www.pearsonglobaleditions.com/gaddis).)

> **TIP:** Read the contents of the `WorldSeriesWinners.txt` file into a list.
When the user enters the name of a team, the program should step through the
list, counting the number of times the selected team appears.

### Exercise 11 - Lo Shu Magic Square
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in
Figure 7-8. The Lo Shu Magic Square has the following properties:

* The grid contains the numbers 1 through 9 exactly.
* The sum of each row, each column, and each diagonal all add up to the same
number. This is shown in Figure 7-9.

In a program you can simulate a magic square using a two-dimensional list. Write
a function that accepts a two-dimensional list as an argument and determines
whether the list is a Lo Shu Magic Square. Test the function in a program.

<table>
    <tbody>
        <tr>
            <td>4</td>
            <td>9</td>
            <td>2</td>
        </tr>
        <tr>
            <td>3</td>
            <td>5</td>
            <td>7</td>
        </tr>
        <tr>
            <td>8</td>
            <td>1</td>
            <td>6</td>
        </tr>
    </tbody>
</table>

Sums are all 15.
