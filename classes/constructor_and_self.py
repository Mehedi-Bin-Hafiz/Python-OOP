
class FullName:

    def __init__(self,name='mehedi',age = 30):
        self.name = name
        self.age = age

    def compare(self,other_object):

        if self.age == other_object.age:
            return True
        else:
            return False

obj1 = FullName() #obj1 automatically call __init__ . init take obj1 by self parameter automatically
obj2 = FullName() # same as obj1

obj1.age = 20
obj2.age = 20

if obj1.compare(obj2):  #obj1 object pass as a parameter by compare's self parameter and obj2 pass by compare method's other_parameter
    print('age are same')
else:
    print('Age Not same')



