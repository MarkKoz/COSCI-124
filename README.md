# CO SCI 124 - Final
**Course Title:** Python Programming<br/>
**Section:** 28314<br/>
**Instructor:** Mohamad Pashazadeh Monajem<br/>
**Semester:** Fall 2017 (2017-08-28 to 2017-12-17)<br/>
**Textbook:** [Gaddis, Tony. _Starting out with Python_. 3rd ed.](http://www.mypearsonstore.com/bookstore/starting-out-with-python-subscription-0133743691)
(ISBN-13: 978-0-13-374369-2)

### Chapter 10
#### Exercise 01 - `Pet` Class
Write a class named `Pet`, which should have the following data attributes:

* `__name` (for the name of a pet)
* `__animal_type` (for the type of animal that a pet is. Example values are
'Dog', 'Cat', and 'Bird')
* `__age` (for the pet's age)

The Pet class should have an `__init__` method that creates these attributes. It
should also have the following methods:

* `set_name`
    * This method assigns a value to the `__name` field.
* `set_animal_type`
    * This method assigns a value to the `__animal_type` field.
* `set_age`
    * This method assigns a value to the `__age` field.
* `get_name`
    * This method returns the value of the `__name` field.
* `get_animal_type`
    * This method returns the value of the `__animal_type` field.
* `get_age`
    * This method returns the value of the `__age` field.

Once you have written the class, write a program that creates an object of the
class and prompts the user to enter the name, type, and age of his or her pet.
This data should be stored as the object's attributes. Use the object's accessor
methods to retrieve the pet's name, type, and age and display this data on the
screen.

#### Exercise 02 - `Car` Class
Write a class named `Car` that has the following data attributes:

* `__year_model` (for the car's year model)
* `__make` (for the make of the car)
* `__speed` (for the car's current speed)

The `Car` class should have an `__init__` method that accepts the car's year
model and make as arguments. These values should be assigned to the object's
`__year_model` and `__make` data attributes. It should also assign 0 to the
`__speed` data attribute.

The class should also have the following methods:

* accelerate
    * The `accelerate` method should add 5 to the speed data attribute each time
    it is called.
* brake
    * The `brake` method should subtract 5 from the speed data attribute each
    time it is called.
* get_speed
    * The `get_speed` method should return the current speed.

Next, design a program that creates a `Car` object and then calls the
`accelerate` method five times. After each call to the `accelerate` method, get
the current speed of the car and display it. Then call the `brake` method five
times. After each call to the `brake` method, get the current speed of the car
and display it.

### Chapter 11
#### Exercise 01 - `Employee` and `ProductionWorker` Classes
Write an `Employee` class that keeps data attributes for the following pieces of
information:

* Employee name
* Employee number

Next, write a class named `ProductionWorker` that is a subclass of the
`Employee` class. The `ProductionWorker` class should keep data attributes for
the following information:

* Shift number (an integer, such as 1, 2, or 3)
* Hourly pay rate

The workday is divided into two shifts: day and night. The shift attribute will
hold an integer value representing the shift that the employee works. The day
shift is shift 1 and the night shift is shift 2. Write the appropriate accessor
and mutator methods for each class.

Once you have written the classes, write a program that creates an object of the
`ProductionWorker` class and prompts the user to enter data for each of the
object's data attributes. Store the data in the object and then use the object's
accessor methods to retrieve it and display it on the screen.

### Chapter 12
#### Exercise 01 - Recursive Printing
Design a recursive function that accepts an integer argument, `n`, and prints
the numbers 1 up through `n`.

#### Exercise 02 - Recursive Multiplication
Design a recursive function that accepts two arguments into the parameters `x`
and `y`. The function should return the value of `x` times `y`. Remember,
multiplication can be performed as repeated addition as follows:

`7 × 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4`

(To keep the function simple, assume that `x` and `y` will always hold positive
nonzero integers.)

### Chapter 13
#### Exercise 01 - Name and Address
Write a GUI program that displays your name and address when a button is
clicked. The program's window should appear as the sketch on the left side of
Figure 13-26 when it runs. When the user clicks the Show Info button, the
program should display your name and address, as shown in the sketch on the
right of the figure.

##### Figure 13-26
![Figure 13-26](https://i.imgur.com/4zIkaXc.png)&nbsp;
![Figure 13-26](https://i.imgur.com/bsvuhYK.png)
