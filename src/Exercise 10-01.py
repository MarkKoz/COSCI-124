#
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name;
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


#
import pet

def main():
    #
    pet_name = ""
    pet_type = ""
    pet_age = 0

    #
    pet_name = input('Enter the name of the pet: ')
    pet_type = input('Enter the type of animal: ')
    pet_age = int(input('Enter the age of the pet: '))

    #
    mypet = pet.Pet(pet_name, pet_type, pet_age)

    #
    print ('Here is the data that you entered: ')
    print ('Pet name: ', mypet.get_name())
    print ('Animal type: ', mypet.get_animal_type())
    print ('Age of pet: ', mypet.get_age())

#
main()
