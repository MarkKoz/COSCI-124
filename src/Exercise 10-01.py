# A class which has accessor and mutator functions for its fields. The values
# which are passed to the constructor are assigned to the fields of the class.
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
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

# Not needed since the class is in the same module as main().
# import pet

def main():
    # Redundantly declares and initialises variables to "empty" values.
    pet_name = ""
    pet_type = ""
    pet_age = 0

    # Variables are set to something useful - the user's inputs.
    pet_name = input('Enter the name of the pet: ')
    pet_type = input('Enter the type of animal: ')
    pet_age = int(input('Enter the age of the pet: '))

    # Construct and retrieve an instance of the class Pet, passing the user's
    # inputs above to its constructor.
    mypet = Pet(pet_name, pet_type, pet_age)

    # Demonstrates that the Pet class was constructed successfully - that the
    # arguments used for the constructor did get stored in the classes's fields.
    # This is done by using accessor methods to retrieve those field's values
    # and then printing them to the console.
    print('Here is the data that you entered: ')
    print('Pet name: ', mypet.get_name())
    print('Animal type: ', mypet.get_animal_type())
    print('Age of pet: ', mypet.get_age())

# Calls the main function when the program runs.
main()
