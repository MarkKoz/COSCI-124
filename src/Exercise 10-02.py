#
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model;
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -=5

    def get_speed(self):
        return self.__speed


#
import car

def main():
    #
    my_car = car.Car('2008', 'Honda Accord')

    #
    print('car is accelerating: ')
    for i in range(5):
        my_car.accelerate()
        print ('Current speed: ', my_car.get_speed())
    print()

    #
    print ('car is braking: ')
    for i in range(5):
        my_car.brake()
        print ('Current speed: ', my_car.get_speed())

#
main()
