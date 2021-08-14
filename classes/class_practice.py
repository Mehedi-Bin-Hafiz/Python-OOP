
class Computer():

    def config(self):
        print('ig, 16gb, 1TB')

com1 = Computer() #com1 is instance of Computer class

Computer.config(com1) # this com1 arguments catch by self

## another way

com1.config() # behind the seen python config take com1 as arguments and pass self parameter.


