#Sometimes you won’t know ahead of time how many arguments a function
#needs to accept. Fortunately, Python allows a function to collect an arbitrary
#number of arguments from the calling statement

def make_pizza(*toppings): ## * automatically make a tuples of all arguments
    """Print the tuples of toppings that have been requested."""
    print(toppings)

#The asterisk in the parameter name *toppings tells Python to make an
#empty tuple called toppings and pack whatever values it receives into this tuple
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#####Mixing Positional and Arbitrary Arguments#######

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')