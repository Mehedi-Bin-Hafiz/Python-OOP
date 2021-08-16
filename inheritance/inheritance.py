# If the class you’re writing is a specialized version of another class you wrote,
# you can use inheritance.

#When one class inherits from another, it automatically takes
#on all the attributes and methods of the first class.
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)  ## here make , model, year belongs to this class parameter
        #he super() function is a special function that helps Python make connections between the parent and child class






##This line tells Python to call the __init__() method from ElectricCar’s parent class, which gives an
#ElectricCar instance all the attributes of its parent class.

my_tesla = ElectricCar('tesla', 'model s', 2016)
desName = my_tesla.get_descriptive_name()
print(desName)
