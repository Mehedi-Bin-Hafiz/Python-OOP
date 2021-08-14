
def myFunction(username): #The variable username in the definition of greet_user() is an example of a parameter
    print('Hello',username)

myFunction('mehedi') #here 'mehedi' is a argument.
#An argument is a piece of information that is passed from a function call to a function.

### positional Arguments ####

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

## keyword arguments ###
#A keyword argument is a name-value pair that we pass to a function

describe_pet(pet_name='coco',animal_type='dog')

## default value ##

#######################VVI#######################
# parameter sequence = positional , default, Arbitrary Arguments, Arbitrary keyword Arguments

def describe_pet(animal_type, pet_name = 'coco'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', )
describe_pet('dog', 'willie')