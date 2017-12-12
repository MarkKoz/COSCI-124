# A class representing a car, which takes a make and model year.
# Has functions simulating acceleration and braking, which modify a field that
# keeps track of the car's speed.
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model # Removed trailing semicolon.
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


# Not needed since the class is in the same module as main().
#import car

def main():
    # Removed module qualifier for same reason as removing the import.
    # Constructs and retrieves an instance to a Car class with the given
    # arguments.
    my_car = Car('2008', 'Honda Accord')

    # Calls the accelerate function on the car instance 5 times, bringing the
    # total speed to 25. Prints the current speed for every iteration of the
    # loop i.e. the new speed after each acceleration.
    print('car is accelerating: ')
    for i in range(5):
        my_car.accelerate()
        print('Current speed: ', my_car.get_speed())
    print()

    # Calls the brake function on the car instance 5 time, bringing the total
    # speed to 0. Prints the current speed for every iteration of the loop i.e.
    # the new speed after each brake.
    print('car is braking: ')
    for i in range(5):
        my_car.brake()
        print('Current speed: ', my_car.get_speed())

# Calls the main function when the program runs.
main()
