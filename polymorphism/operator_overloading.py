
a = 3
b = 4

print(a+b)
print(int.__add__(a,b))
print((a.__add__(b)))
# in python everything belongs to object so object refers to class and class has method.
# when we a+b behind the scene it call __add__ method of int class


######## operator overloading ##########

class Student():

    def __init__(self,M1, M2):
        self.M1 = M1
        self.M2 = M2

    def __add__(self, other):
        s1_mark = self.M1 + self.M2
        s2_mark = other.M1 + other.M2

        return s1_mark + s2_mark


s1 = Student(10,20)
s2 = Student(5,10)

## s1, s2 belongs to a a class. so we can add s1 and s2 but there is no add method in my custom class
# if i write my custom __add__ class then it called operator overloading

print(s1 + s2) # this is operator overloading 




