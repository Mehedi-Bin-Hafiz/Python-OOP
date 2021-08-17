# Making an object from a class is called instantiation, and you work with
# instances of a class.

#### when we write function in a class then it called method
# ((Methods are associated with the objects of the class they belong to.
# Functions are not associated with any object. We can invoke a function just by its name.
# Functions operate on the data you pass to them as arguments.))
#### Variables that are accessible through instances like this are called attributes.

###The __init__() method at is a special method
#Python runs automatically whenever we create a new instance of a class

def call_able():
    pass

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name #Variables that are accessible through instances like this are called attributes.
        self.age = age
        ##Any variable prefixed with self is available to every method in the class, and we’ll also be
        ##able to access these variables through any instance created from the class.

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


### __init___###
#it must be included in the definition because when Python calls this __init__() method later (to create an
#instance of Dog), the method call will automatically pass the self argument.

#### VVI####
#Every method call associated with a class automatically passes self, which
#is a reference to the instance itself; it gives the individual instance access to
#the attributes and methods in the class.

if __name__ == '__main__':
    my_dog = Dog('willie', 6) #When Python reads this line, it calls the __init__() method in Dog with the arguments 'willie' and 6.
    #We store that instance in the variable my_dog.

    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")

    my_dog.sit()
    my_dog.roll_over()
