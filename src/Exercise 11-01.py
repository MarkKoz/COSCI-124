class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        # Calls the base class's constructor.
        Employee.__init__(self, name, id_number)

        # Declares and initialises fields using the constructor arguments.
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Mutator functions for class fields. Sets the fields to the given values.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Accessor functions for class fields. Returns the values of the fields.
    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate

# Not needed since the class is in the same module as main().
# import emp

def main():
    # Redundantly declares and initialises variables to "empty" values.
    worker_name= ''
    worker_id = ''
    worker_shift = 0
    worker_pay = 0.0

    # Variables are set to something useful - the user's inputs.
    worker_name = input('Enter the name: ')
    worker_id = input('Enter the ID number: ')
    worker_shift = int(input('Enter the shift number: '))
    worker_pay = float(input('Enter the hourly pay rate: '))

    # Removed module qualifier for same reason as removing the import.
    # Constructs and retrieves an instance to a ProductionWorker using the
    # user's inputs as arguments for the constructor.
    worker = ProductionWorker(worker_name, worker_id, # Removed backslash.
                              worker_shift, worker_pay)

    # Demonstrates that the ProductionWorker was successfully constructed and
    # contains the proper values by accessing and print its fields through the
    # accessor functions. Also demonstrates that the class does inherit its
    # base class's (Employee) functions (get_name() and get_id_number()).
    print('Production worker information:')
    print('Name:', worker.get_name())
    print('ID number:', worker.get_id_number())
    print('Shift:', worker.get_shift_number())
    print('Hourly Pay Rate: $', # Removed unnecessary backslash.
          format(worker.get_pay_rate(), ',.2f'), sep = '')

# Calls the main function when the program runs.
main()
